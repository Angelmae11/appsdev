<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup Form</title>
</head>
<body>
    <h2>Signup Form</h2>

    <form method="post" action="signup.php">

        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required
               pattern="(?=.*[a-z])(?=.*[A-Z]).{6,12}"
               title="Password must be between 6 and 12 characters, contain at least one uppercase and one lowercase letter"><br><br>

        <input type="submit" value="Signup">
    </form>
</body>
</html>
