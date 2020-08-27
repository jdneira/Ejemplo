# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:59:41 2020

@author: Javiera Parodi
"""
# Ayudantía 2

# Ejercicio 1

# Resultado esperado
# Film;Opening Weekend;Worldwide Gross;Budget

# Comienza escribiendo aquí tu código
archivo=open("datos_peliculas.csv","r")
lineas=archivo.readlines()
archivo.close()
linea1=lineas[0]
print(linea1)


    
# Abre el archivo, carga los datos e imprime la primera línea

# No olvides cerrar el archivo


###############################################

# Ejercicio 2
# Resultado esperado
# The To-Do List;1579402;3566225;1.5

# Funciones recomendadas
# split --> Separar una línea (string) en una lista
# replace --> Reemplazar un caracter por otro dentro de un string
# No olvides considerar los \n dentro de tu código

# Escribe tu código acá
film=[]
opening=[]
world=[]
budget=[]
lista_2=[]
for i in lineas:
    m=i.split(";")
    lista_2.append(m)

for i in lista_2:
    film.append(i[0])
    opening.append(i[1])
    world.append(i[2])
    budget.append(i[3])
    
opening_new=[]
world_new=[]
budget_new=[]
    
for i in opening:
    m=i.replace(".","")
    opening_new.append(m)
    
for i in world:
    l=i.replace(".","")
    world_new.append(l)

world_new2=[]   
for i in world_new:
    p=i.replace(",","")
    world_new2.append(p)

for i in budget:
    t=i.replace(",",".")
    budget_new.append(t)
    
budget_new2=[]    
for i in budget_new:
    t=i.replace("\n","")
    budget_new2.append(t)

lineas_listas=[] 
lista_final=[]
for i in range(len(film)):
    lista=[]
    lineas_listas.append(film[i]+";"+opening_new[i]+";"+ world_new2[i]+";"+budget_new2[i])
    lista.append(film[i])
    lista.append(opening_new[i])
    lista.append(world_new2[i])
    lista.append(budget_new2[i])
    lista_final.append(lista)
    
print(lineas_listas[4])

###############################################

# Ejercicio 3
# Funciones recomendadas
# join --> Unir los elementos de una lista en un string
# No olvides cerrar el archivo

# Escribe tu código acá
lista_final2=[]
for i in lista_final:
    suma=0
    for j in i:
        if j=="-" or j=="" or j=="n/a":
            suma+=1

    if suma==0:
        lista_final2.append(i)
    else:
        pass
  
final=[]
for i in lista_final2:
    final.append(i[0]+";"+i[1]+";"+i[2]+";"+i[3]+"\n")
      
archivo_corregido=open("films_corregido_Javiera_Neira.csv","w")

for i in final:
    archivo_corregido.write(i)
archivo_corregido.close()
        


    


    

            
    

            
        