import time

print('d̴͓͔͇̾͐̕o̸̢̫͔͛̈́͠n̸͕̻͇͌͑͒g̵̠̙̫͛̓̀a̵̙͍͓̔̽́t̴̟͖̪̾͘ö̴̡͕͓́̀͊ \n' )

print('TODOS LOS DERECHOS RESERVADOS\n' )


print('Segun los campos de tu base de datos EJ-> tra_id(tra)')
print('Ingresa algun subfijo para lo realizado EJ(Trabajadores -> Tra)')
print('Segun los campos de tu base de datos EJ-> tra_id(tra)')
subfijo=input("Ingrese el subfijo : \n")
Nombre=input("Ingrese el Nombre : \n")
N_variable = int(input('Ingrese la cantidad de variables: \n'))
ArrayVariables = []
for i in range(1,N_variable+1):
	dato=input("Ingrese el nombre de la variable N->"+ str(i) + ' : \n')
	
	ArrayVariables.append(dato)

							#Funcion CrearModelo
###################################################################################
def CrearModelo(ArrayVariables,subfijo,validacionDePost,Nombre):
	archivo = open("model"+str(Nombre)+".php","w")
	archivo = open("model"+str(Nombre)+".php","a")
	archivo.write('<?php\n')
	archivo.write('\n')
	archivo.write('require_once "mainModel.php";\n')
	archivo.write('\n')
	archivo.write('class '+str(Nombre)+'Modelo extends mainModel{\n')
	archivo.write('\n')
	archivo.write('protected static function agregar_'+str(Nombre)+'_modelo($datos){\n')	
	archivo.write('$sql=mainModel::conectar()->prepare("INSERT INTO '+str(Nombre)+'(\n')	

	#$sql=mainModel::conectar()->prepare("INSERT INTO dependencia(dp_nombre,dp_direccion,dp_fono1,dp_fono2,dp_encargado,dp_email,e_id,id_comunas) VALUES 
	#(:nombre,:direccion,:fono1,:fono2,:encargado,:email,:empresa,:comuna)");

	
	for i in range(N_variable-1):
		archivo.write(subfijo+'_'+str(ArrayVariables[i])+',\n')

	archivo.write(str(subfijo+'_'+ArrayVariables[N_variable-1])+'\n')

	archivo.write(')\n')

	archivo.write(' VALUES ( \n')
	
	for i in range(N_variable-1):
		archivo.write(':'+str(ArrayVariables[i])+',\n')
	
	archivo.write(':'+str(ArrayVariables[N_variable-1])+'\n')
	archivo.write(')"')
	archivo.write(');\n')



	for i in range(N_variable):
		archivo.write('$sql->bindParam(":'+str(ArrayVariables[i])+'",$datos["'+str(ArrayVariables[i])+'"]);\n')

	archivo.write('$sql->execute();\n')
	archivo.write('return $sql;\n')	
	archivo.write('}\n')		
	archivo.write('}\n')


							#Funcion CrearControlador
###################################################################################

def CrearControlador(ArrayVariables,subfijo,validacionDePost,Nombre):
	archivo = open("controlador"+str(Nombre)+".php","w")
	archivo = open("controlador"+str(Nombre)+".php","a")
	archivo.write('<?php\n')
	archivo.write('\n')
	archivo.write('require_once "../modelos/model'+str(Nombre)+'.php";\n')
	archivo.write('\n')
	archivo.write('class '+str(Nombre)+'Controlador extends '+str(Nombre)+'Modelo{\n')
	archivo.write('\n')
	archivo.write('public function agregar_'+str(Nombre)+'_controlador(){\n')
	archivo.write('\n')	
	for i in range(N_variable):
		archivo.write('$'+str(ArrayVariables[i])+'=mainModel::limpiar_cadena($_POST["'+subfijo+'_'+str(ArrayVariables[i])+'"]);\n')

	archivo.write('$datos_'+str(Nombre)+'_reg=[\n')


	for i in range(N_variable-1):
		archivo.write('"'+str(ArrayVariables[i])+'"=>$'+str(ArrayVariables[i])+',\n')



	archivo.write('"'+str(ArrayVariables[N_variable-1])+'"=>$'+str(ArrayVariables[N_variable-1])+'\n')

	
	archivo.write('];\n')
	archivo.write('\n')
	archivo.write('$agregar_'+str(Nombre)+'='+str(Nombre)+'Modelo::agregar_'+str(Nombre)+'_modelo($datos_'+str(Nombre)+'_reg);\n')	
	archivo.write('if($agregar_'+str(Nombre)+'->rowCount()==1){\n')
	archivo.write('echo "WORK!";\n')
	archivo.write('}else{\n')
	archivo.write('NO FUNCIONO\n')
	archivo.write('}\n')
	archivo.write('}\n')








def CrearVista(ArrayVariables,subfijo,Nombre):
	archivo = open(str(Nombre)+".php","w")
	archivo = open(str(Nombre)+".php","a")
	archivo.write('<html>\n')
	archivo.write('<head>\n')
	archivo.write('<title></title>\n')
	archivo.write('</head>\n')
	archivo.write('<body>\n')
	archivo.write('<form method="POST" action="">\n')

	for i in range(N_variable):
		archivo.write('<input type="text" name="' +subfijo+'_'+str(ArrayVariables[i])+'">\n')

	
	validacionDePost = subfijo+'_'+str(ArrayVariables[1])
	archivo.write('<!DOCTYPE html>\n')
	archivo.write('<button type="submit">Ingresar</button>\n')
	archivo.write('</form>\n')
	archivo.write('</body>\n')
	archivo.write('</html>\n')
	archivo.write('<?php\n')
	archivo.write('if(isset($_POST[\''+validacionDePost+'\'])){\n')
	archivo.write('require_once "Controlador'+str(Nombre)+'.php";\n')
	archivo.write('$'+subfijo+'= new '+str(Nombre)+'Controlador();\n')
	archivo.write('echo $'+subfijo+'->agregar_'+str(Nombre)+'_controlador();\n')
	archivo.write('}\n')
	archivo.write('?>\n')
	archivo.close()

	CrearControlador(ArrayVariables,subfijo,validacionDePost,Nombre)
	CrearModelo(ArrayVariables,subfijo,validacionDePost,Nombre)




CrearVista(ArrayVariables,subfijo,Nombre)



print('10 % ')
print('20 % ')
print('36 % ')
print('48 % ')
print('56 % ')
time.sleep(2)
print('90 % ')
print('100 % ')

