<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - My Website</title>

    <style>
        
        body {
            margin: 0;
            font-family: "Poppins", Arial, sans-serif;
            background: linear-gradient(135deg, #4facfe, #00f2fe);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
        }

        
        .container {
            background: #ffffff;
            width: 400px;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            text-align: center;
            animation: fadeIn 0.8s ease-in-out;
        }

       
        h1 {
            margin-bottom: 10px;
            font-size: 28px;
            color: #1d1d1d;
        }

        p {
            margin-bottom: 30px;
            color: #555;
        }

        
        a {
            display: inline-block;
            margin: 10px;
            padding: 12px 35px;
            background: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 50px;
            font-size: 16px;
            transition: 0.3s;
        }

        a:hover {
            background: #0056b3;
            transform: scale(1.06);
        }

        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
    </style>

</head>
<body>

    <div class="container">
        <h1>Welcome to My Website</h1>
        <p>Please choose an action below:</p>

        <a href="login.php">Login</a>
        <a href="signup.php">Sign Up</a>
    </div>

</body>
</html>
