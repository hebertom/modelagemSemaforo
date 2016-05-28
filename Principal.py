from Semaforo import Semaforo
from Queue import Queue
import time
import random
import sys

class Principal():

    s1 = Semaforo(True)
    s2 = Semaforo(False)
    s3 = Semaforo(True)
    s4 = Semaforo(False)


    fila1 = Queue()
    fila2 = Queue()
    fila3 = Queue()
    fila4 = Queue()
    
    aux = int(raw_input("Digite o numero de carros a serem sorteados: "))

    i = 0
    
    while(i <= aux):
        prox_carro = random.randint(1,4)
        if(prox_carro == 1):
            fila1.insert(fila1)
            s1.addNumCarros()
        elif(prox_carro == 2):
            fila2.insert(fila2)
            s2.addNumCarros()
        elif(prox_carro == 3):
            fila3.insert(fila3)
            s3.addNumCarros()
        else:
            fila4.insert(fila4)
            s4.addNumCarros()
        i = i + 1

    print("Semaforo 1: " + str(s1.getNumCarros()) + " Carros")
    print("Semaforo 2: " + str(s2.getNumCarros()) + " Carros")
    print("Semaforo 3: " + str(s3.getNumCarros()) + " Carros")
    print("Semaforo 4: " + str(s4.getNumCarros()) + " Carros")

    n1 = s1.getNumCarros()
    n2 = s2.getNumCarros()
    n3 = s3.getNumCarros()
    n4 = s4.getNumCarros()

    i = True
    inicio = time.time()
    while i :   
        sys.stdout.flush()
        time.sleep(2)

        if s1.getEstado():
            print("Semaforos 1 e 3 abertos")
        if s2.getEstado():
            print("Semaforos 2 e 4 abertos")

        if s1.getEstado():
            s1.removeCarro()
        if s2.getEstado():
            s2.removeCarro()
        if s3.getEstado():
            s3.removeCarro()
        if s4.getEstado():
            s4.removeCarro()

        s1.mudaEstado()
        s2.mudaEstado()
        s3.mudaEstado()
        s4.mudaEstado()

        q1 = s1.estaVazio()
        q2 = s2.estaVazio()
        q3 = s3.estaVazio()
        q4 = s4.estaVazio()

        if q1 and q2 and q3 and q4:
            fim = time.time()
            tempo = fim - inicio
            i = False
            print("----- Todos os carros passaram -----")
            print("Tempo total: " + str(tempo) + " seg")
            print("Tempo Medio S1: " + str(n1 / tempo) + " seg")
            print("Tempo Medio S2: " + str(n2 / tempo) + " seg")
            print("Tempo Medio S3: " + str(n3 / tempo) + " seg")
            print("Tempo Medio S4: " + str(n4 / tempo) + " seg")

           
    