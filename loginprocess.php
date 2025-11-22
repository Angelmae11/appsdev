<?php
session_start();

// Hardcoded credentials (example only)
$valid_username = 'admin';
$valid_password = 'admin123';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $username = trim($_POST['username']);
    $password = trim($_POST['password']);

    // Validate login
    if ($username === $valid_username && $password === $valid_password) {

        $_SESSION['username'] = $username;

        header("Location: protected.php");
        exit;

    } else {
        // Return with error message
        header("Location: login.php?error=1");
        exit;
    }

} else {
    header("Location: login.php");
    exit;
}
