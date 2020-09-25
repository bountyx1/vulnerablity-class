<!DOCTYPE html>
<?php
session_start();
if (!isset($_SESSION['loggedIn']) && !$_SESSION['loggedIn'] == true) {
	header("Location: index.html");
}
$username = $_SESSION['username'];
setcookie("user", base64_encode($username));
header("Content-Security-Policy: frame-ancestors 'none'");
$username = $_GET['username'];
?>
<html>

<head>
	<title>Web Page</title>
	<meta charset="utf-8">
	<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
</head>

<body>
	<p id='xss' onclick="tryXSS()">Click Me </p>
	<?php
	session_destroy();
	?>
</body>
<script>
	function tryXSS() {
		var test = "<?php echo htmlspecialchars($username); ?>";
		document.getElementById("xss").innerHTML = test;
	}
</script>

</html>