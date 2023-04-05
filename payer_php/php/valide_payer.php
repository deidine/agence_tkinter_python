<?php
include_once "database.php";



    $id=$_GET['id'];
  
  $sql=  "UPDATE `client` SET `payer` = '✅' WHERE `id` = '$id'";
$resul =mysqli_query($conx,$sql);
if ($resul==true) {
    header("Location: ../index.html");
    # code...
}else{
    echo "<h2>dont updated.....!</h2>";   
}
    # code...
?>