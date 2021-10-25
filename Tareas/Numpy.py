#NAME
#       Numpy.py
#VERSION
#        [1.0]
#AUTHOR
#        Adrian Prieto Castellanos <<adrianpc@lcg.unam.mx>>
#DESCRIPTION
#        Hacemos arrays estructurados a partir de los arrays vistos en clase
#CATEGORY
#        Numpy.
#INPUT
#        Dos arrays estructurados 
#OUTPUT
#        Tres arrays estructurados y uno normal 
#EXAMPLES
#        Input:
#            produccion = np.array([[5, 3], [11, 7], [4, 9], [2, 6]])
#            costos = np.array([3.5, 5, 7, 4.3])
#        Output:
#            Costos por G/l 
#            [[0.7        0.45454545 1.75       2.15      ]
#             [1.16666667 0.71428571 0.77777778 0.71666667]]
#                Arrays estructurados 
#                 Produccion 
#             [('Gen1',  5, 3) ('Gen2', 11, 7) ('Gen3',  4, 9) ('Gen4',  2, 6)]
#                Costos 
#             [('Gen1', 3.5) ('Gen2', 5. ) ('Gen3', 7. ) ('Gen4', 4.3)]
#                Costos por G/l 
#             [('Gen1', 0.7     , 1.1666667 ) ('Gen2', 0.454545, 0.71428571)
#                ('Gen3', 1.75    , 0.7777778 ) ('Gen4', 2.15    , 0.71666667)]
#GITHUB
#        https://github.com/adrianpriet/Python-2-class/tree/main/Tareas
import numpy as np

# Arrays de la clase 
produccion = np.array([[5, 3], [11, 7], [4, 9], [2, 6]])
print("Produccion \n", produccion)
costos = np.array([3.5, 5, 7, 4.3])
print("Costos" , "\n", costos)
costosgl = costos/produccion.T
print("Costos por G/l", "\n", costosgl)
# Arrays estructurados
produccion_estruct = np.array([("Gen1", 5, 3), ("Gen2", 11, 7), ("Gen3", 4, 9), ("Gen4", 2, 6)],
                                   dtype=[('nombre del gen', (np.str_, 10)), ("30 celsius", np.int32), ("35 celsius", np.int32)])

costos_estruct = np.array([("Gen1", 3.5), ("Gen2", 5), ("Gen3", 7), ("Gen4", 4.3)],
                         dtype=[("Nombre del gen", (np.str_, 10)), ("Costo de induccion", np.float64)])
costosgl_estruct = np.array([("Gen1",0.7,1.1666667), ("Gen2", 0.454545,0.71428571), ("Gen3", 1.75, 0.7777778), ("Gen4", 2.15, 0.71666667)],
                          dtype=[('nombre del gen', (np.str_, 10)), ("costo 30 celsius", np.float64), ("costo 35 celsius", np.float64)])
print("Arrays estructurados \n","Produccion \n", produccion_estruct)
print("Costos \n",costos_estruct)
print("Costos por G/l \n", costosgl_estruct)
