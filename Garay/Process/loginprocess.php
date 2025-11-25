<?php
session_start();
include "db_connect.php"; // your database connection file

$login_id = $_POST['login_id'];
$password = $_POST['password'];


$query = $conn->prepare("SELECT * FROM users WHERE email = ? OR username = ?");
$query->bind_param("ss", $login_id, $login_id);
$query->execute();
$result = $query->get_result();

if ($result->num_rows === 1) {
    $user = $result->fetch_assoc();

 
    if (password_verify($password, $user['password'])) {

        
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];

        header("Location: dashboard.php");
        exit;
    }
}


header("Location: login.php?error=1");
exit;
?>
