###Utilizar el metodo format() mas complejo
##Esxcribir un progrma que permita FORMATEAR la cadena de caracteres:
	#Me llamo \\\\\\\ y tengo \\\\\\  a;os de edad y estoy aprendiendo el lenguaje \\\\\\\\\ 
	#el progamadebe permitir formatear esta cadena asignadoles un valor a las vareables:
		#mi NOMBRE , EDAD , LENGAJE
		
miNombre = "JULIO CESAR"
edad = 30
lenguaje = "python"

ch = f"Me llamo {miNombre} y tengo{edad} años. Estoy aprendiendo".format(miNombre, edad)+\
         f"el lenguaje {lenguaje}". format(lenguaje)
print(ch)