#Classe principal que realizará o gerenciamento do semáforo e dos carros

#                |      |
#                |    f2|
# _______________|    s2|____________
#           f1 s1
#                        s3 f3
# _______________        ____________
#                |s4    |
#                |f4    |
#                |      |

import Semaforo
import Carro
import Queue
import time
import random

class Principal():

    s1 = Semaforo(True)
    s2 = Semaforo(False)
    s3 = Semaforo(True)
    s4 = Semaforo(False)


    fila1 = Queue
    fila2 = Queue
    fila3 = Queue
    fila4 = Queue

    while True :
        inicio = time.time()

        while True:
            fim = time.time()

            if (fim - inicio) > 2000:
                s1.mudaEstado()
                s2.mudaEstado()
                s3.mudaEstado()
                s4.mudaEstado()
                break
            #Fazer a lógica de chegar carros aleatóriamente em todas as filas
            prox_carro = random.randint(1,4)
            if(prox_carro == 1):
                fila1.insert()
                break
            elif(prox_carro == 2):
                fila2.insert()
                break
            elif(prox_carro == 3):
                fila3.insert()
                break
            else:
                fila4.insert()
                break
    