###invertir una cadena de caracter3s

###cr3ar, ob5ener, exportar,etc lista de tuplas

F = [('pera',30), ('sandia',50),('jamon',25),('melon',15),('pastax',15)]
##ordenar la lista d3 tuplas acendentemente 
## en funcion del segundo el3mente de las tuplas
F.sort(key = lambda x : x[1])
print(F)