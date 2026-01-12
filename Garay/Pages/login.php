<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <style>
        body {
            margin: 0;
            font-family: "Poppins", Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            background: #ffffff;
            width: 450px;
            padding: 35px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            animation: fadeIn 0.8s ease-in-out;
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #1d1d1d;
        }

        label {
            font-weight: 600;
        }

        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 15px;
            transition: 0.3s;
        }

        input:focus {
            border-color: #007bff;
            outline: none;
            box-shadow: 0 0 5px rgba(0,123,255,0.3);
        }

        button {
            width: 100%;
            padding: 12px;
            background: #007bff;
            border: none;
            color: white;
            font-size: 17px;
            border-radius: 50px;
            cursor: pointer;
            transition: 0.3s;
            margin-top: 10px;
        }

        button:hover {
            background: #0056b3;
            transform: scale(1.04);
        }

        .links {
            text-align: center;
            margin-top: 20px;
        }

        .links a {
            color: #007bff;
            text-decoration: none;
        }

        .links a:hover {
            text-decoration: underline;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
    </style>

</head>
<body>

    <div class="container">
        <h2>Login</h2>

        <form method="post" action="login_process.php">

            <label>Email or Username</label>
            <input type="text" name="login_id" placeholder="Email or username" required>

            <label>Password</label>
            <input type="password" name="password" required>

            <button type="submit">Login</button>

            <div class="links">
                <p>Don't have an account? <a href="signup.php">Sign up here</a></p>
                <p><a href="index.php">Back to Home</a></p>
            </div>

        </form>
    </div>

</body>
</html>
