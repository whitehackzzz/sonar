<?php
// Vulnerable PHP script

// SQL Injection Vulnerability
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$user_input = $_GET['username']; // Potentially malicious user input
$sql = "SELECT * FROM Users WHERE username = '$user_input'";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Name: " . $row["username"]. "<br>";
    }
} else {
    echo "0 results";
}
$conn->close();

// XSS Vulnerability
$user_input2 = $_GET['name']; // Potentially malicious user input
echo "Hello, " . $user_input2 . "!"; // Output user input without sanitization

// Remote Code Execution Vulnerability
$cmd = $_GET['cmd']; // Potentially malicious user input
eval($cmd); // Evaluates and executes user input directly

?>
