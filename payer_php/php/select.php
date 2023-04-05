<?php 
session_start();


$conx=mysqli_connect("localhost","root","","agencetk");

$rtSql = "Select * ,c.id as clnt_id,p.id pay_id from payer p inner join client c on p.telephone=c.telephone order by p.id desc";
    $resultrtSql = mysqli_query($conx, $rtSql);
    $arr = array();
    $json = array();
    if(mysqli_num_rows($resultrtSql)){
        while($row = mysqli_fetch_assoc($resultrtSql))
        $row2[]=$row;
        // array_push($json, array($row['Seat_No'], $row['Occupied'],$row['Gender']));
        // $routeJson = json_encode($arr);
    }
    if(!empty($row2)){
        $result['type'] = "success";
        $result['result'] = $row2;
        }else{
        $result['type'] = "error";
        $result['result'] = "No result found";
        }

        echo json_encode($row2);
      mysqli_close($conx);
    // }
    //   // else{ header("Location: ../../../index.html");
    //   //   }
    //     else {echo json_encode('login');}
        ?>