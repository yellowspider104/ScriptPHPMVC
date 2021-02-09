<?php

require_once "../modelos/modelusuario.php";

class usuarioControlador extends usuarioModelo{

public function agregar_usuario_controlador(){

$usuario=mainModel::limpiar_cadena($_POST["u_usuario"]);
$clave=mainModel::limpiar_cadena($_POST["u_clave"]);
$nombre=mainModel::limpiar_cadena($_POST["u_nombre"]);
$perfil=mainModel::limpiar_cadena($_POST["u_perfil"]);
$estado=mainModel::limpiar_cadena($_POST["u_estado"]);
$foto=mainModel::limpiar_cadena($_POST["u_foto"]);
$datos_usuario_reg=[
"usuario"=>$usuario,
"clave"=>$clave,
"nombre"=>$nombre,
"perfil"=>$perfil,
"estado"=>$estado,
"foto"=>$foto
];

$agregar_usuario=usuarioModelo::agregar_usuario_modelo($datos_usuario_reg);
if($agregar_usuario->rowCount()==1){
echo "WORK!";
}else{
NO FUNCIONO
}
}
