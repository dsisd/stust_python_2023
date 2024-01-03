<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library System - Main</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <script src="main.js"></script>
    <style>
        /* Add some styling for the buttons */
        nav {
            text-align: center;
            margin: 20px 0;
        }

        nav a {
            margin: 0 10px;
            text-decoration: none;
            padding: 5px 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            color: #333;
        }

        /* Style for logout link */
        body {
            overflow: hidden;
            /* Prevents horizontal scrollbar due to float */
        }

        .logout-link {
            float: right;
            margin-right: 20px;
            /* Adjust the margin as needed */
        }
    </style>
</head>

<body>
    <!-- Navigation bar with buttons -->
    <nav>
        <a href="main.php">首頁</a>
        <a href="booklist.html">館藏資訊</a>
        <a href="availableBooks.html">借書系統</a>
        <a href="borrowedBooks.html">歸還系統</a>
        <a href="logout.php" class="logout-link">Logout</a>
        <h2>Welcome </h2>
        <h2>~圖書館借用系統~</h2>
    </nav>


    <div id="book-list">
        <!-- Book list will be displayed here -->
    </div>

    </form>
</body>

</html>