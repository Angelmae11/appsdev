<?php
session_start(); 

$valid_username = 'admin';
$valid_password = 'admin123';


if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $username = $_POST['username'];
    $password = $_POST['password'];

   
    if ($username == $valid_username && $password == $valid_password) {
      
        $_SESSION['username'] = $username;
        
       
        header('Location: protected.php');
        exit;
    } else {
       
        header('Location: login.php?error=1');
        exit;
    }
} else {
   
    header('Location: login.php');
    exit;
}