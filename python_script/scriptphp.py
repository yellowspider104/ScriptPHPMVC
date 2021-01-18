import time

print('d̴͓͔͇̾͐̕o̸̢̫͔͛̈́͠n̸͕̻͇͌͑͒g̵̠̙̫͛̓̀a̵̙͍͓̔̽́t̴̟͖̪̾͘ö̴̡͕͓́̀͊ \n' )




print('Segun los campos de tu base de datos EJ-> tra_id(tra)')
print('Ingresa algun subfijo para lo realizado EJ(Trabajadores -> Tra)')
print('Segun los campos de tu base de datos EJ-> tra_id(tra)')
subfijo=input("Ingrese el subfijo : \n")
N_variable = int(input('Ingrese la cantidad de variables: \n'))
ArrayVariables = []
for i in range(1,N_variable+1):
	dato=input("Ingrese el nombre de la variable N->"+ str(i) + ' : \n')
	
	ArrayVariables.append(dato)


def CrearVista(ArrayVariables,subfijo):
	archivo = open("example.php","w")
	archivo = open("example.php","a")
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
	archivo.write('require_once "Controlador.php";\n')
	archivo.write('$'+subfijo+'= new Controlador();\n')
	archivo.write('echo $'+subfijo+'->AgregarUsuario();\n')
	archivo.write('}\n')
	archivo.write('?>\n')




	archivo.close()

CrearVista(ArrayVariables,subfijo)

print('10 % ')
print('20 % ')
print('36 % ')
print('48 % ')
print('56 % ')
time.sleep(2)
print('90 % ')
print('100 % ')

