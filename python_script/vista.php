<?php 


 ?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form method="POST" action="">
		<input type="text" name="sas">
		<button type="submit" >Ingresar</button>
	</form>

</body>
</html>
<?php
	


	if(isset($_POST['sas'])){
        /*----------instancia a controlador----------*/
        require_once "Controlador.php";
        $ins_documento = new Controlador();
    
        /*----------agregar un usuario----------*/
        
            echo $ins_documento->AgregarUsuario();
        
    }
    ?>
