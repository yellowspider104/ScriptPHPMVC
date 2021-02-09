<html>
<head>
<title></title>
</head>
<body>
<form method="POST" action="">
<input type="text" name="u_usuario">
<input type="text" name="u_clave">
<input type="text" name="u_nombre">
<input type="text" name="u_perfil">
<input type="text" name="u_estado">
<input type="text" name="u_foto">
<!DOCTYPE html>
<button type="submit">Ingresar</button>
</form>
</body>
</html>
<?php
if(isset($_POST['u_clave'])){
require_once "Controladorusuario.php";
$u= new usuarioControlador();
echo $u->Agregarusuario();
}
?>
