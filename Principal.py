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











