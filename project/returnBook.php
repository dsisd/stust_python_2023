<?php
require 'db.php';

// 假設你有資料庫連線，從查詢參數中取得書名
$title = $_GET['title'];

// 使用者名稱（用實際的欄位名稱替換 'your_username_column'）
$username = ''; // 用實際的使用者名稱取得邏輯替換
$status = 'available';
$query = "UPDATE books SET username='$username', status='$status' WHERE title='$title'";


// 執行查詢
$result = mysqli_query($conn, $query);

// 檢查查詢是否成功
if ($result) {
    echo json_encode(['success' => true, 'message' => '書籍歸還成功。']);
} else {
    echo json_encode(['success' => false, 'message' => '歸還書籍時發生錯誤。']);
}

// 如果需要，關閉你的資料庫連線
mysqli_close($conn);
