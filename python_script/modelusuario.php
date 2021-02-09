<?php

require_once "mainModel.php";

class usuarioModelo extends mainModel{

protected static function agregar_usuario_modelo($datos){
$sql=mainModel::conectar()->prepare("INSERT INTO usuario(
u_usuario,
u_clave,
u_nombre,
u_perfil,
u_estado,
u_foto
)
 VALUES ( 
:usuario,
:clave,
:nombre,
:perfil,
:estado,
:foto
)");
$sql->bindParam(":usuario",$datos["usuario"]);
$sql->bindParam(":clave",$datos["clave"]);
$sql->bindParam(":nombre",$datos["nombre"]);
$sql->bindParam(":perfil",$datos["perfil"]);
$sql->bindParam(":estado",$datos["estado"]);
$sql->bindParam(":foto",$datos["foto"]);
$sql->execute();
return $sql;
}
}
