<?php
$user = array("name"=>"navjeet", "email"=>"test@navjeet.com", "csrf-token"=>md5("admin"));

header("Content-Type: application/javascript");
if(isset($_GET["callback"]))
{

echo $_GET['callback']."(".json_encode($user).")";

}
else
{
echo "test(".json_encode($user).")";
}


?>
 

