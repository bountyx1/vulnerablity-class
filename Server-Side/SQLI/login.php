<?php

include('config.php');

if (isset($_REQUEST['login'])) {
    $mysqli =  new mysqli($hostname, $username, $password, $database);

    if ($mysqli == false) {
        die("Error could not connect" . mysqli_connect_error());
    }

    $uname = $_POST['username'];
    $passwd = $_POST['password'];

    $query = "select * from users where name = '$uname' and password = '$passwd'";
    //$query = "select * from users where name = '"."$uname" ."' and password = '"."$passwd"."'";
    
    $result = mysqli_query($mysqli,$query);
   
    $count = mysqli_num_rows($result);
    //$row = mysqli_fetch_array($result);

    if($count){
        echo "<h1>Hacking krta ha bsdiwala :| </h1>";
    }
    else{
        echo "<h1> Chal bsdk </h1>";
    }

}

?>