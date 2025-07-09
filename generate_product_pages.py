import os
import re
import json
import ast

DETAILS_DIR = 'products/details'
TEMPLATE_FILE = 'products/product-template.html'
OUTPUT_DIR = 'products'
PRODUCTS_JS = 'assets/js/products.js'


def parse_details(filepath):
    data = {}
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()
    key = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.match(r'^\w+:', line):
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            if value:
                data[key] = value
            else:
                data[key] = []
        elif line.startswith('-') and key:
            if isinstance(data[key], list):
                data[key].append(line[1:].strip())
    return data

def render_list(items):
    return '\n          '.join(f'<li>{item}</li>' for item in items)

def update_products_js(products):
    PRODUCTS_JS = "assets/js/products.js"  # Adjust path as needed
    
    print(f"Attempting to update {PRODUCTS_JS}")
    print(f"Products to update: {len(products)}")
    
    # Check if file exists
    if not os.path.exists(PRODUCTS_JS):
        print(f"ERROR: {PRODUCTS_JS} does not exist!")
        return
    
    # Read the existing products.js file
    try:
        with open(PRODUCTS_JS, encoding='utf-8') as f:
            js_content = f.read()
        print("Successfully read products.js")
    except Exception as e:
        print(f"ERROR reading {PRODUCTS_JS}: {e}")
        return

    # Find the products array with more flexible regex
    match = re.search(r'const\s+products\s*=\s*(\[[\s\S]*?\]);', js_content, re.DOTALL)
    if not match:
        print("ERROR: Could not find products array in products.js")
        return
    
    print("Found products array in JavaScript file")
    
    # Parse the existing array
    existing_array_str = match.group(1)
    existing_products = []
    
    try:
        # Method 1: Try to parse as JSON (double quotes)
        json_str = existing_array_str.replace("'", '"')
        existing_products = json.loads(json_str)
        print(f"Parsed {len(existing_products)} existing products using JSON")
    except Exception as json_error:
        print(f"JSON parsing failed: {json_error}")
        try:
            # Method 2: Try to evaluate as Python literal (handles single quotes)
            existing_products = ast.literal_eval(existing_array_str)
            print(f"Parsed {len(existing_products)} existing products using AST")
        except Exception as ast_error:
            print(f"AST parsing failed: {ast_error}")
            try:
                # Method 3: Use regex to extract individual objects
                existing_products = parse_js_array_regex(existing_array_str)
                print(f"Parsed {len(existing_products)} existing products using regex")
            except Exception as regex_error:
                print(f"Regex parsing failed: {regex_error}")
                print("Starting with empty products array")
                existing_products = []

    # Build a dict for quick lookup by url
    existing_by_url = {p.get("url"): p for p in existing_products if "url" in p}
    
    # Create updated products list - start with ALL existing products
    updated_products = existing_products.copy()
    print(f"Starting with {len(updated_products)} existing products")
    
    # Track URLs of existing products
    existing_urls = {p.get("url") for p in existing_products if p.get("url")}
    print(f"Existing URLs: {existing_urls}")
    
    # Process each new product from .txt files
    for new_prod in products:
        new_url = new_prod["url"]
        print(f"Processing new product: {new_prod.get('name', 'Unknown')} at {new_url}")
        
        if new_url in existing_urls:
            # Update existing product
            for i, existing_prod in enumerate(updated_products):
                if existing_prod.get("url") == new_url:
                    # Merge: keep existing fields, update with new data
                    merged_prod = existing_prod.copy()
                    merged_prod.update(new_prod)
                    updated_products[i] = merged_prod
                    print(f"Updated existing product: {merged_prod.get('name', 'Unknown')}")
                    break
        else:
            # Add new product
            updated_products.append(new_prod)
            print(f"Added new product: {new_prod.get('name', 'Unknown')}")

    print(f"Final products count: {len(updated_products)}")

    # Format the new array as JS with proper Unicode handling
    new_array = "const products = " + json.dumps(
        updated_products, 
        indent=2, 
        ensure_ascii=False  # This prevents Unicode escaping
    ) + ";"

    # Replace the old array with the new one
    new_js_content = js_content[:match.start()] + new_array + js_content[match.end():]

    # Write back to products.js
    try:
        with open(PRODUCTS_JS, 'w', encoding='utf-8') as f:
            f.write(new_js_content)
        print(f"SUCCESS: Updated {PRODUCTS_JS} with merged product cards.")
    except Exception as e:
        print(f"ERROR writing to {PRODUCTS_JS}: {e}")
        return

def parse_js_array_regex(array_str):
    """
    Fallback method to parse JavaScript array using regex
    This is a simple implementation - might need refinement for complex objects
    """
    products = []
    
    # Remove outer brackets and split by object boundaries
    content = array_str.strip()[1:-1]  # Remove [ and ]
    
    # Simple regex to find object boundaries (this is basic and might need improvement)
    objects = re.findall(r'\{[^{}]*\}', content)
    
    for obj_str in objects:
        try:
            # Convert JS object notation to Python dict
            obj_str = obj_str.replace("'", '"')  # Replace single quotes with double quotes
            obj_str = re.sub(r'(\w+):', r'"\1":', obj_str)  # Add quotes around keys
            product = json.loads(obj_str)
            products.append(product)
        except:
            continue
    
    return products

def main():
    with open(TEMPLATE_FILE, encoding='utf-8') as f:
        template = f.read()

    products = []
    for filename in os.listdir(DETAILS_DIR):
        if not filename.endswith('.txt'):
            continue
        details = parse_details(os.path.join(DETAILS_DIR, filename))
        html = template
        # Replace simple fields
        for field in ['title', 'slug', 'price', 'image', 'description', 'benefits_intro', 'get_started']:
            html = html.replace(f'{{{{{field}}}}}', details.get(field, ''))
        # Replace list fields
        for field in ['key_features', 'benefits', 'system_requirements']:
            html = html.replace(f'{{{{{field}}}}}', render_list(details.get(field, [])))
        # Output file
        slug = details.get('slug', filename[:-4])
        output_path = os.path.join(OUTPUT_DIR, f'{slug}.html')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Generated {output_path}')
        # Prepare product card info for products.js
        product_card = {
            "name": details.get("title", ""),
            "price": details.get("price", ""),
            "url": f"./products/{slug}.html",
            "image": details.get("image", ""),
            "description": details.get("description", "")[:180]
        }
        products.append(product_card)
    # Update products.js
    update_products_js(products)

if __name__ == '__main__':
    main() 