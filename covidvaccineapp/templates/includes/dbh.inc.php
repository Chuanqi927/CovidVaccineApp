<?php

$db_server_name = "localhost";
$db_user_name = "root";
$db_password = "";
$db_name = "covidvaccineapp";

//create connection
$connection = mysqli_connect($db_server_name, $db_user_name, $db_password, $db_name);

// if(mysqli_connect_errno()){
//     echo "failed to connect to database";
//     exit;
// }

// echo "Connected to Database Successfully!";