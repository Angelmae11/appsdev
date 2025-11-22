<?php
session_start(); 


if (!isset($_SESSION['username'])) {
    
    header('Location: login.php?error=2');
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Protected Page</title>
    <link rel="stylesheet" href="style.css"> 
</head>
<body>
    <div class="protected-container">
        <h2>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>!</h2>
        <p>This is a protected page, only accessible to logged-in users.</p>
        <a href="logout.php">Logout</a>
    </div>
</body>
</html>