
import numpy as np
import matplotlib.pyplot as plt


def entrenamiento ():
   #Perceptron harlim
    #numero_iteraciones = int(input("Digita el numero de iteraciones que te gustarian, obvio un numero positivo y mayor a 0: "))
    print ("---------------------------------------------------------")
    valor_p1 = int(input("Digite el valor  del P1: "))
    valor2_p1 = int(input("Digite el segundo valor  del P1: "))
    print ("El P1 los valores: ",  "[", valor_p1 ,"]"  , "[", valor2_p1 , "]")
    print ("---------------------------------------------------------")
    valor_p2 = int(input("Digite el valor  del P2: "))
    valor2_p2 = int(input("Digite el segundo valor  del P2: "))
    print ("El P2 los valores: ",  "[", valor_p2 ,"]"  , "[", valor2_p2 , "]" )
    print ("---------------------------------------------------------")
    valor_p3 = int(input("Digite el valor  del P3: "))
    valor2_p3 = int(input("Digite el segundo valor  del P3: "))
    print ("El P3 los valores: ",  "[", valor_p3 ,"]"  , "[", valor2_p3 , "]" )
    print ("---------------------------------------------------------")
    valor_p4 = int(input("Digite el valor  del P4: "))
    valor2_p4 = int(input("Digite el segundo valor  del P4: "))
    print ("El P4 los valores: " ,  "[", valor_p4 ,"]"  , "[", valor2_p4 , "]" )
    print ("---------------------------------------------------------")
    
    valor_t1 = int(input("Digite el valor  del t1: "))
    valor_t2 = int(input("Digite el valor  del t2: "))
    valor_t3 = int(input("Digite el valor  del t3: "))
    valor_t4 = int(input("Digite el valor  del t4: "))
    print ("El valor de tus t's son: " ,  "[", valor_t1 ,"]"  , "[", valor_t2 , "]" ,  "[", valor_t3 ,"]"  , "[", valor_t4 , "]" )
    
    valor_peso1 = float(input("Digite el valor  del peso (w1): "))
    valor_peso2= float(input("Digite el valor  del peso (w2): "))
    w=np.transpose(np.array([valor_peso1, valor_peso2])) # Declara el peso y hace transpuesta
    
    b = float(input("Digite el valor  de la ganancia (b) : "))
    
    a = 0
    total_errores = 0
    
    while total_errores != 4: #Funcion que determina el numero de iteraciones
        
        matriz = [ #Declara a los patrones
	    [valor_p1, valor_p2, valor_p3, valor_p4],
	    [valor2_p1, valor2_p2, valor2_p3, valor2_p4]
    ]
       
        arreglo = [valor_t1,valor_t2,valor_t3,valor_t4] # Declara las t de los respectivos patrones
        j = 0
        total_errores = 0
        print ("-------------------------")
        print ("Iteracion numero ----------------> ", {a+1})
        a += 1
        errores = []
        for i in arreglo:
            patron = [fila[j] for fila in matriz]
            print ("-------------------------")
            print ("Esta en el patron:", patron)
            print ("-------------------------")
            array = (w*np.transpose(np.array(patron)))
            a1 = (array[0] + array[1] + b)
            if (a1 >= 0):
                a1 = 1
            else:
                a1 = 0 
            e1 = (i - a1)
            errores.append(e1)
            if (e1 != 0):
                w = (w+(e1*np.transpose(np.array(patron))))
                b = (b+e1)
                print("(Cambio de valores en el peso)")
                print ("Nuevo valor de W: ", w)
                print ("Nuevo valor de B: ", b)
                j +=1
            else:
                print("(No cambiaron los valores en el peso)")
                print ("Nuevo valor de W: ", w)
                print ("Nuevo valor de B: ", b)
                j +=1
                total_errores += 1

        print("Te mostraré los números que representan los errores: ")
        for numero in errores:
            print(numero)
        #errores.index(0)
                   
    else:
        print("Se acabo :( ")
        x1= (-b/array[0])
        print ("El eje de las X, tiene un valor de: ", x1)
        y1= (-b/array[1])
        print ("El eje de las Y, tiene un valor de: ", y1)
        #x = [0,0,1,1]
        #y = [0,1,0,1]
        x = [valor_p1,valor_p2,valor_p3,valor_p4]
        y = [valor2_p1,valor2_p2,valor2_p3,valor2_p4]
        plt.plot(x1, y1 , lw = 2 , color = 'black')
        plt.scatter(x,y)
        plt.show()


def entrenamiento2 ():
   #Perceptron harlimsimetrico
    #numero_iteraciones = int(input("Digita el numero de iteraciones que te gustarian, obvio un numero positivo y mayor a 0: "))
    print ("---------------------------------------------------------")
    valor_p1 = int(input("Digite el valor  del P1: "))
    valor2_p1 = int(input("Digite el segundo valor  del P1: "))
    print ("El P1 los valores: ",  "[", valor_p1 ,"]"  , "[", valor2_p1 , "]")
    print ("---------------------------------------------------------")
    valor_p2 = int(input("Digite el valor  del P2: "))
    valor2_p2 = int(input("Digite el segundo valor  del P2: "))
    print ("El P2 los valores: ",  "[", valor_p2 ,"]"  , "[", valor2_p2 , "]" )
    print ("---------------------------------------------------------")
    valor_p3 = int(input("Digite el valor  del P3: "))
    valor2_p3 = int(input("Digite el segundo valor  del P3: "))
    print ("El P3 los valores: ",  "[", valor_p3 ,"]"  , "[", valor2_p3 , "]" )
    print ("---------------------------------------------------------")
    valor_p4 = int(input("Digite el valor  del P4: "))
    valor2_p4 = int(input("Digite el segundo valor  del P4: "))
    print ("El P4 los valores: " ,  "[", valor_p4 ,"]"  , "[", valor2_p4 , "]" )
    print ("---------------------------------------------------------")
    
    valor_t1 = int(input("Digite el valor  del t1: "))
    valor_t2 = int(input("Digite el valor  del t2: "))
    valor_t3 = int(input("Digite el valor  del t3: "))
    valor_t4 = int(input("Digite el valor  del t4: "))
    print ("El valor de tus t's son: " ,  "[", valor_t1 ,"]"  , "[", valor_t2 , "]" ,  "[", valor_t3 ,"]"  , "[", valor_t4 , "]" )
    
    valor_peso1 = float(input("Digite el valor  del peso (w1): "))
    valor_peso2= float(input("Digite el valor  del peso (w2): "))
    w=np.transpose(np.array([valor_peso1, valor_peso2])) # Declara el peso y hace transpuesta
    
    b = float(input("Digite el valor  de la ganancia (b) : "))
    
    a = 0
    total_errores = 0
    
    while total_errores != 4: #Funcion que determina el numero de iteraciones
        
        matriz = [ #Declara a los patrones
	    [valor_p1, valor_p2, valor_p3, valor_p4],
	    [valor2_p1, valor2_p2, valor2_p3, valor2_p4]
    ]
       
        arreglo = [valor_t1,valor_t2,valor_t3,valor_t4] # Declara las t de los respectivos patrones
        j = 0
        total_errores = 0
        print ("-------------------------")
        print ("Iteracion numero ----------------> ", {a+1})
        a += 1
        errores = []
        for i in arreglo:
            patron = [fila[j] for fila in matriz]
            print ("-------------------------")
            print ("Esta en el patron:", patron)
            print ("-------------------------")
            array = (w*np.transpose(np.array(patron)))
            a1 = (array[0] + array[1] + b)
            if (a1 >= 0):
                a1 = 1
            else:
                a1 = -1 
            e1 = (i - a1)
            errores.append(e1)
            if (e1 != 0):
                w = (w+(e1*np.transpose(np.array(patron))))
                b = (b+e1)
                print("(Cambio de valores en el peso)")
                print ("Nuevo valor de W: ", w)
                print ("Nuevo valor de B: ", b)
                j +=1
            else:
                print("(No cambiaron los valores en el peso)")
                print ("Nuevo valor de W: ", w)
                print ("Nuevo valor de B: ", b)
                j +=1
                total_errores += 1

        print("Te mostraré los números que representan los errores: ")
        for numero in errores:
            print(numero)
        #errores.index(0)
                   
    else: #Enmantenimiento para futuras actulizaciones
       print("Se acabo :( ")
       x1= (-b/array[0])
       print ("El eje de las X, tiene un valor de: ", x1)
       y1= (-b/array[1])
       print ("El eje de las Y, tiene un valor de: ", y1)
       #x = [0,0,1,1]
       #y = [0,1,0,1]
       x = [valor_p1,valor_p2,valor_p3,valor_p4]
       y = [valor2_p1,valor2_p2,valor2_p3,valor2_p4]
       plt.plot(x1, y1 , lw = 2 , color = 'black')
       plt.scatter(x,y)
       plt.show()





#menu para elegir opcion
opcion = int(input("Digite su opcion a elegir;  {1.- Perceptron en hardlim}       {2.- Perceptron en harlimsimetrico} "))
    
if (opcion == 1):
    entrenamiento()
elif (opcion == 2):
    entrenamiento2()
