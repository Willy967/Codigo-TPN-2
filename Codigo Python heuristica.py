from arbol3x3 import Nodo
import copy

def busqueda_heuristica(e_inicial,e_final):
    exito=False
    nodos_frontera=[]
    nodos_visitados=[]
    #creacion del primer nodo inicial o un objeto de tipo nodo
    NodoInicial=Nodo(e_inicial)
    nodos_frontera.append(NodoInicial)
    comparaciones=0
    textoError=""
    while len(nodos_frontera)!=0 and (not exito)
    #nodo es el Nodo padre inicialmente y nodos_fronteras llegaria a ser una cola porque 
    #saca el primero que estuvo en la cola y asi sucesivamte
       nodo=nodos_frontera.pop(0)
       nodos_visitados.append(nodo)
       print("Vuelta = ", comparaciones)
       if nodo.obtener_datos()==e_final:
           exito=True
           print("Cantidad de comparaciones: ", comparaciones)
           return nodo
       else:
           comparaciones+=1
           aux=nodo.obtener_datos()
           fila=0
           columna=0
           x=len(aux) 
           y=len(aux[0]) 
           
           for i in range(x):
               for j in range(y):
                   if aux[i][j]==0:
                       fila=icolumna=j
                       break
            nodos_hijos=[]
            #hallamos el centro de la matriz
            if fila==columna and (fila+columna)==2:
               mataux = nodoresltante3x3(copy.deepcopy(aux),fila,columna,0,-1) #mover el cero a la izquierda       
               nodo_izquierdo=Nodo(mataux)
               nodo_izquierdo.asignar_coste( costodelnodo(e_final,mataux) )
               
               mataux =nodoresultante3x3(copy.deepcopy(aux),fila,columna,-1,0) #movemos el cero arriba
               nodo_arriba=Nodo(mataux)
               nodo_arriba.asignar_coste( costodelnodo(e_final,mataux) )
               
               mataux=nodoresultante3x3(copy.deepcopy(aux),fila,columna,0,1) #movemos el cero a la derecha
               nodo_derecho=nodo(mataux)
               nodo_derecho.asignar_coste( costedelnodo(e_final,mataux) )
               
               mataux = nodoresultante3x3(copy.deepcopy(aux),fila,columna,1,0) #movemos el cero abajo
               nodo_abajo=Nodo(mataux)
               nodo_abajo.asignar_coste( costodelnodo(e_final, mataux) )
               
               if nodo_izquierdo.en_lista(nodos_visitados) ==False:
                   nodos_hijos.append(nodo_izquierdo)
               if nodo_arriba.en_lista(nodos_visitados) == False: 
                   nodos_hijos.append(nodo_arriba)
               if nodo_derecho.en_lista(nodos_visitados) == False:
                   nodos_hijos.appened(nodo_abajo)
               #BUSCAMOS EL NODO CON MAYOR ITEMS EN COMUN
               nodo_elegido=buscar_nodo_elegido(nodos_hijos)
               nodos_frontera.appened(nodo_elegido)
               try:
                   nodo.asignar_hijos([nodo_elegido])      
               except:
                   textoerror="Sin Nodos, No Solucionado"
                   break
            elif fila==1 or columna==1:
                #Buscamos si en uno de los centros laterales esta el cero
                #clon = copy.deepcopy(aux)
                if fila==1:  #detecta que los ceros esten en uno de los 4 centros
                
                      nodo_arriba=nodoresultante3x3(copy.deepcopy(aux),fila,columna,-1,0) # movemos cero hacia arriba
                      nodo_abajo=nodoreultante3x3(copy.deepcopy(aux),fila,columna,1,0) #movemos cero hacia abajo
                     
                      if fila > columna:
                          nodo_centro=nodoresultante3x3(copy.deepcopy(aux),fila,columna,0,1) #movemos cero hacia el centro
                      else:
                          nodo_centro=nodoresultante3x3(copy.deepcopy(aux),fila,columna,0,-1) # movemos cero hacia el centro
                      nodo_A=Nodo(nodo_arriba)
                      nodo_A.asignar_coste( costodelnodo(e_final,nodo_arriba) ) 
                      nodo_B=Nodo(nodo_abajo)
                      nodo_B.asignar_coste( costodelnodo(e_final,nodo_abajo) )
                      nodo_C=Nodo(nodo_centro)
                      nodo_C.asignar_coste( costodelnodo(e_final,nodo_centro) )  
                      if nodo_A.en_lista(nodos_visitados) == False:
                          nodos_hijos.append(nodo_A)    
                      if nodo_B.en_lista(nodos_visitados) == False:
                          nodos_hijos.append(nodo_B) 
                      if nodo_C.en_lista(nodos_visitados) == False:
                          nodos_hijos.append(nodo_C) 
                else:
                    nodo_izquierda = nodoresultante3x3(copy(aux),fila,columna,0,-1)  # mover cero  la izquierda
                    nodo_derecha = nodoresultante3x3(copy.deepcopy(aux),fila,columna,0,1)  # mover cero a la derecha
                    if columna>fila:
                        nodo_centro= nodoresultante3x3(copy.deepcopy(aux),fila,columna,1,0)  # mover cero al centro
                    else:
                        nodo_centro= nodoresultante3x3(copy.deepcopy(aux),fila,columna,-1,0) # mover cero hacia el centro
                    nodo_I=Nodo(nodo_izquierda)
                    nodo_I.asignar_coste( costodelnodo(e_final,nodo_izquierda) )
                    nodo_C=Nodo(nodo_centro)
                    nodo_C.asignar_coste( costodelnodo(e_final,nodo_centro) )
                    nodo_D=Nodo(nodo_derecha) 
                    Nodo_D.asignar_coste( costodelnodo(e_final,nodo_derecha) ) 
                    if nodo_I.en_lista(nodos_visitados) == False :
                        nodos_hijos.append(nodo_I)
                    if nodo_C.en_lista(nodos_visitados) == False :
                        nodos_hijos.append(nodo_C)
                    if nodo_D.en_lista(nodos_visitados) == False :
                        nodos_hijos.append(nodo_D) 52:03                      
                nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_D)
                try:
                    nodo.asignar_hijos([nodo_elegido])
                except:
                    textoError="Sin Nodos, No solucionado"
                    break
            else:
                # vemos si en una de las esquina esta el cero
                if fila<=columna and (fila+columna)<len(aux) : # para los ceros que estan en las esquinas superiores
                    # ESQUINAS
                    nodo_abajo= nodoresultante3x3(copy.deepcopy(aux),fila,columna,1,0) #mueve cero hacia abajo
                    if columna<=fila:
                        nodo_lado=nodoresultante3x3(copy.deepcopy(aux)fila,columna,0,1) #mueve el cero al lado derecho
                    else:
                        nodo_lado = nodoresultante3x3(copy.deepcopy(aux)fila,columna,0,-1) #mueve cero al lado izquierdo
                    nodo_A = Nodo(nodo_abajo)
                    nodo_A.asignar_coste( costodelnodo(e_final,nodo_abajo) ) 
                    nodo_L=Nodo(nodo_lado)
                    nodo_L.asignar_coste( costodelnodo(e_final,nodo_lado) )
                    if nodo_A.en_lista(nodos_visitados) == False:
                        nodos_hijos.append(nodo_A)
                else: #ceros que estan en las esquinas inferiores
                    nodo_arriba=nodoresltante3x3(copy.deepcopy(aux),fila,columna,-1,0) #mueve cero hacia la izquierda
                nodo_AA = Nodo(nodo_arriba)
                nodo_AA.asignar_coste( costodelnodo( e_final,nodo,arriba) )
                nodo_AAA=Nodo(nodo_abajo)
                nodo_AAA.asignar_coste( costodelnodo(e_final,nodo,abajo) )
                if nodo_AA.en_lista(nodos_visitados) == False:
                    nodos_hijos.append(nodo_AA)
                if nodo_AAA.en_lista(nodos_visitados) ==False:
                    nodos_hijos.append(nodo_AA)
                nodo_elegido=buscar_nodo_elegido(nodos_hijos)
                nodos_frontera.append(nodo_elegido)
                try:
                    nodo.asignar_hijos([nodo_elegido]) 
                except:
                    textoError="Sin Nodos, No solucionado"
                    break           
                