<?php
$ip = '192.168.1.5'
$port = '8723';

$led = $_POST['led'];
$action = $_POST['action'];

$msg = $led +'~'+$action;

$client = stream_socket_client($ip . ":" . $port, $errno, $errorMessage);
if ($client === false) {
//$_SESSION["msg"] .= "<br/>Cannot connect to Judge: Contact Admin";
}
fwrite($client, $msg);
fclose($client);
>