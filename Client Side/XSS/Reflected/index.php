<!DOCTYPE html>
<html>
<body>

<p id="demo" onclick="myFunction()">Click Me</p>

<script>
function myFunction() {
var x = '<?php echo htmlspecialchars($_GET["xss"],ENT_QUOTES); ?>';
document.getElementById("demo").innerHTML = x;

}
</script>

</body>
</html> 





