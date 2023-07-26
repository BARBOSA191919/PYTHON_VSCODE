#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("¿Cuántos años tienes? ")) # se crea la variable edad y se pregunta al usuario los años 
for i in range(age): # for con variable i que tenga el rango de la variable anterior que es age
    print("Has cumplido " + str(i+1) + " años") # mostramos con print la edad y que se muestre con str la cadena de caracteres de los años que cumplio cada año

