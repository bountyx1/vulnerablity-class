<?php
session_start();

$uname = "admin";
$passwd = "secret";

$username = $_GET['username'];
$password = $_GET['password'];

if ($username == $uname && $password == $passwd) {
	$_SESSION['loggedIn'] = true;
	$_SESSION['username'] = $username;
	header("Location: backend.php");
} else {
	//echo "<script>alert('Wrong Creds')</script>";
	header("Location: index.html");
}
