
<?php
require 'db.php';

$sql = "SELECT * FROM books WHERE status = 'available'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $books = array(); // Create an array to store the messages

    while ($row = $result->fetch_assoc()) {
        $book = array(
            "title" => $row["title"],
            "author" => $row["author"],
            "status" => $row["status"],
            "timestamp" => $row["timestamp"]
        );

        $books[] = $book; // Add each message to the array
    }

    echo json_encode($books); // Encode the array into JSON
} else {
    echo json_encode(array("message" => "No messages found.")); // Encode a message in case no records are found
}

$conn->close();
?>