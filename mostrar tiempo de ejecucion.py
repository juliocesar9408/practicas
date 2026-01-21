import time

##memorizar la hora de inicio del prgrama
inicio = time.time()

##NUESTRO  CODIGO ##

for i in range(0,11) :
	print("8x", i,"=", 8*i)
#######################

## memorizar la hora de finaizacion del prohgrama

final = time.time()

## calcuar el tiempo de ejecucion 

print("tiempo de ejecicion del codigo :",final-inicio)