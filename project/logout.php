<?php
// logout.php

// Start or resume the session
session_start();

// Clear all session data
session_unset();

// Destroy the session
session_destroy();

// Redirect to login page
header("Location: login.html");
exit();
