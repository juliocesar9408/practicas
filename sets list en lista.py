###precencia de un elemento en una lista

###creacion de una funcion python 
def verifpresencia (a,L) : 
   ###si el elemento esta precente en la lista L 
   if a in L:
   	##entonces devovemos true
   	return True
   	##caso contrario 
   else:
   	### devolvemos false
   	return False
   	
### invocamos la funcion 
 ## verifprecencia(2,[1,2,3,4,5,6])
verifpresencia(-1,[3,6,9,7,"abcr"])
print(verifpresencia (a,L))