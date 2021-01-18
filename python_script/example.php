<html>
<head>
<title></title>
</head>
<body>
<form method="POST" action="">
<input type="text" name="tra_nombre">
<input type="text" name="tra_apellido">
<input type="text" name="tra_edad">
<!DOCTYPE html>
<button type="submit">Ingresar</button>
</form>
</body>
</html>
<?php
if(isset($_POST['tra_apellido'])){
require_once "Controlador.php";
$tra= new Controlador();
echo $tra->AgregarUsuario();
}
?>
