<?php

// Secure email subscription handler
session_start();

// Generate CSRF token if not exists
if (!isset($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
}

// Check if request is POST and CSRF token is valid
if ($_SERVER["REQUEST_METHOD"] == "POST" && 
    isset($_POST['csrf_token']) && 
    hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'])) {
    
    // Validate and sanitize input
    $email = filter_var(trim($_POST['email_address']), FILTER_SANITIZE_EMAIL);
    
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Check for duplicates
        $file = 'subscribers.txt';
        $existing_emails = [];
        
        if (file_exists($file)) {
            $existing_emails = array_map('trim', file($file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES));
        }
        
        if (in_array(strtolower($email), array_map('strtolower', $existing_emails))) {
            header('Location: index.html?error=duplicate');
            exit();
        }
        
        // Write to file with error handling
        try {
            $result = file_put_contents(
                $file, 
                $email . PHP_EOL, 
                FILE_APPEND | LOCK_EX
            );
            
            if ($result === false) {
                throw new Exception('Failed to write to file');
            }
            
            // Log successful subscription
            error_log("New subscription: $email");
            
            // Redirect with success message
            header('Location: thank-you.html?success=true');
            exit();
            
        } catch (Exception $e) {
            error_log("Subscription error: " . $e->getMessage());
            header('Location: index.html?error=server');
            exit();
        }
        
    } else {
        header('Location: index.html?error=invalid');
        exit();
    }
} else {
    header('Location: index.html?error=security');
    exit();
}