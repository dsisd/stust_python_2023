<?php
require 'db.php';

$sql = "SELECT * FROM books";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $books = array();

    while ($row = $result->fetch_assoc()) {
        $book = array(
            "title" => $row["title"],
            "author" => $row["author"],
            "status" => $row["status"],
            "timestamp" => $row["timestamp"]
        );

        $books[] = $book;
    }

    header('Content-Type: application/json');
    echo json_encode($books);
} else {
    echo json_encode(array("message" => "No books found."));
}

$conn->close();
