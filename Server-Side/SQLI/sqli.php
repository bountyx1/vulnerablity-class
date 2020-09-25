<?php

include('config.php');

if (isset($_REQUEST['login'])) {
    $mysqli =  new mysqli($hostname, $username, $password, $database);

    if ($mysqli == false) {
        die("Error could not connect" . mysqli_connect_error());
    }

    //$id = $_GET['id'];
    //echo "($id)" . "<br>";

    //To try different type of SQLi , make changes here.
    //$sql_querry = "select * from users where id = '$id'";                     //string based && possible cases: ('$id') , '($id)'
    $sql_querry = "select name from users where id = ($id) limit 1";           //int based (concatination also works)  && possible cases : ($id) ,

    $result = $mysqli->query($sql_querry);

    //$row =  $result->fetch_assoc();
    //print_r($row);

    while ($rows = $result->fetch_assoc()) {
        echo "User Name : " . $rows['name'] . "<br>";
    }

    $mysqli->close();

    //header("refresh:2;url=index.html");
}



