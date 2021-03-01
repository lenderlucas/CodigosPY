# def run():
#     #LIMITE = 1000
#     limite_con =int(input('Ingresa el numero a elevar:  '))
#     limite =int(input('Ingresa el valor a elevar:  '))
#     contador=0
#     potencia_2= limite_con**contador

#     while potencia_2 < limite:
#         print(str(limite_con)+ ' elevado a '+ str(contador)+ ' es igual a = '+ str(potencia_2))
#         contador += 1
#         potencia_2 = limite_con**contador




# if __name__ == "__main__":
#     run()

# contador = 0
# for contador in range(1,1000):
#     contador += 1
#     print(contador)
# SE EVALUA EL BUBLE CON LOS NUMEROS PRIMOS 
def es_primo(numero):
    contador=0
    contador2=0

    for i in range(1, numero):
        if i==1 or i==numero:
            continue
        if numero % i ==0:
            contador+=1
    if contador==0:
        return True
    else:
        return False



def run():
    numero =int(input('Escibre un numero para evaluar si es primo o no: '))
    if es_primo(numero):
        print('El numero que ingresaste es primo')
    else:
        print('El numero que ingresaste no es primo')

if __name__ == "__main__":
    run()