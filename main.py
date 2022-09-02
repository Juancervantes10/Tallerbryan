import json

graph={}
cargar= []


usuario = input("Por favor digite su Usuario:")
n = input("aqui puedes ingresar la cantidad de nodos\n")

def llenar(n):
  Menu = True
  while Menu == True:

    opc = int(input("1.Inicio del programa\n2.Consultar las rutas \n3.Salir del programa\n"))
  
    if opc == 1:
    
        nodo_conexiones=[]
        graph.clear()
        print("")
        print("HOLA: " + usuario)
        it_is = False 
        
        while it_is == False:  
            try:
                int(n) 
                it_is = True
            except ValueError: 
                it_is = False
                print("Verifica que el campo no esté vacio e ingrese un numero\n")
                
                n = input("Ingresa la cantidad de nodos\n") 
            
        n = int(n) 
    
        for i in range(n): 
            it_is = False 
    
            while it_is == False: 
                valor=input("Nodo actual "+str(i+1)+"\nDigite el nombre del nodo en mayuscula "+str("    ")).upper()
               
                if valor.isnumeric(): 
                   
                    print("Verifique que el campo ingresado sea un texto y no un numero")
                elif len(valor) <= 0: 
                    print("Llena el campo con una letra")
                   
                else:
                    nodo = valor 
                    it_is = True
    
            estado = True
            while estado == True:
                print(nodo+str(nodo_conexiones)) 
                rpta=input("Que opcion Deseas?\n1.Deseas añadir una conexion al nodo\n2.No deseas añadir conexion al nodo\n3.Requieres deshacer una conexion al nodo\n") #vALIDAR
                if rpta.isalpha():
                    print("Elige la opción con un número")
                else:
                    rpta = int(rpta)
                    if rpta == 1: 
                        print(nodo+str(nodo_conexiones))
                        print("¿A que camino se conecto el nodo "+nodo+"?")
                        nodo_unir=input()
                        nodo_conexiones.append(nodo_unir)
                        
                    if rpta == 2: 
                        estado = False
                    if rpta == 3: 
                        if not nodo_conexiones:
                            
                            print("\nLa lista está vacía\n")
                        else:
                            quitar = input("Digita el camino del nodo que deseas deshacer\n").upper()
                            nodo_conexiones.remove(quitar)
                            
                            print("Se ha eliminado el nodo "+quitar+"\n")                                
            graph.update({nodo: set(nodo_conexiones)})
            nodo_conexiones.clear()
            print(graph)
        vi = input("Ingresa el nodo inicial    ").upper()
        vf = input("Ingresa el nodo final    ").upper()
        busq = list(dfs_paths(graph, vi, vf))
        datos_json(usuario, vi, vf, n, busq)
      
    if opc == 2:
      print("consulta de rutas")
      estado2 = True
      while estado2 == True:
        opcionsubmenu = int(input(" ¿Que acción desea que realice? \n1.Mostrar todos los registros que tengo en JSON\n 2.Regresar al menu principal\n"))
        if opcionsubmenu == 1:
          print("Mostrar todas las consultas JSON")
          mostrar_todo_json()     
          break
        if opcionsubmenu == 2:
          print("Regresar al menú principal")
          break


    if opc == 3:
      print("Saliste")
      exit()
      
def mostrar_todo_json():
  if verificar() == True:
    with open('prueba.json') as archivo:
      jsoninicio = json.load(archivo)
    jsonfinal = json.dumps(jsoninicio, indent = 3)
    return print(str(jsonfinal)) 
    
def dfs_paths(graph, start, goal):

    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]
        for next in graph[node] - set(path):

            if next == goal:
                yield path + [next]
            else:
                stack.append(path + [next])


def verificar():
    try:
        with open ('prueba.json') as archivo:
            return True     
    except FileNotFoundError as e:
        return False

def Datos( usuario, n, vi, vf,  busq):
    nuevodic = {'Usuario': usuario, 'Cantidad de nodos': n ,'Valor inicial': vi, 'Valor final': vf, 'Busqueda': busq}
    return nuevodic

def datos_json( usuario,n, vi, vf, busq):

    if verificar() == True:
        with open ("prueba.json") as archivo:
            datos = json.load(archivo)
        datos.append(Datos(usuario,n, vi, vf,busq))

        with open("prueba.json", 'w') as archivo_nuevo:
            json.dump(datos, archivo_nuevo, indent = 3)
            print("Datos añadidos a "+archivo_nuevo.name)
    else:
        with open("prueba.json", 'w') as archivo_nuevo:
            cargar.append(Datos(usuario, n, vi, vf, busq))
            json.dump(cargar, archivo_nuevo, indent = 3)     
            print("Se ha creado el historial en el archivo " +archivo_nuevo.name)


llenar(n)

         
