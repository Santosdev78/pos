import os

menu=[{'id':1, 'nombre':'Arroz', 'precio':50},
      {'id':2, 'nombre':'Habichuelas', 'precio':80},
      {'id':3, 'nombre':'Aceite', 'precio':300},
      {'id':4, 'nombre':'Pollo', 'precio':85},
      {'id':5, 'nombre':'Lechuga', 'precio':80},]

carrito=[]

def imprimir_menu(menu):
    tammax=0
    for item in menu:
        tamactual=len(str(item['id']))+len(item['nombre'])+len(str(item['precio']))
        if  tamactual>tammax:
            tammax=tamactual
    print('-'*(int(tammax/2+2))+'Menú'+'-'*(int(tammax/2+2)))
    for item in menu:
        print(f'{item['id']}. {item['nombre']} -> RD${item['precio']}')

def buscar_producto(id, menu):
    for item in menu:
        if menu['id']==int(id):
            return menu
        return None
        
        
def agregar_al_carrito (id,cantidad,precio_tot):
    if id == 1:
            carrito.append({"id": 1,"nombre":"arroz","precio":50,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 2:
            carrito.append({"id": 2,"nombre":"habichuelas","precio":80,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 3:
            carrito.append({"id": 3,"nombre":"aceite","precio":300,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 4:
            carrito.append({"id": 4,"nombre":"pollo","precio":85,"cantidad":cantidad,"precio total":precio_tot})
    elif id == 5:
            carrito.append({"id": 5,"nombre":"lechuga","precio":80,"cantidad":cantidad,"precio total":precio_tot})

def imprimirfactura(carrito):
    tamid=1
    tamnombre=1
    tamprecio=1
    for item in carrito:
        tamidact=len(str(item['id']))
        tamnombreact=len(item['nombre'])
        tamprecioact=len(str(item['precio']))
        if tamidact>tamid:
            tamid=tamidact
        if tamnombreact>tamnombre:
            tamnombre=tamnombreact
        if tamprecioact>tamprecio:
            tamprecio=tamprecioact
    if tamid-2<0:
        tamid=1
    else:
        tamid-=2
    if tamnombre-6<0:
        tamnombre=1
    else:
        tamnombre-=6
    if tamprecio-6<0:
        tamprecio=1
    else:
        tamprecio-=6
    print('ID'+' '*(tamid+2)+'Nombre'+' '*(tamnombre+1)+'Precio'+' '*(tamprecio))
    for item in carrito:
        print(str(item['id'])+' '*(tamid+4-len(str(item['id'])))+item['nombre']+' '*(tamnombre+7-len(item['nombre']))+str(item['precio']))

def main(menu):
    opc=" "
    while opc != "S":
        imprimir_menu(menu)
        opc=input("¿Que producto desea agregar? ")
        if opc=="1":
            id=1
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                if vol_agregar == "si":
                    main(menu)
                elif vol_agregar != "si":
                    opc="S"
                    imprimirfactura(carrito)
                    print ("Adios")
        elif opc=="2":
            id=2
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                if vol_agregar == "si":
                    main(menu)
                elif vol_agregar != "si":
                    opc="S"
                    imprimirfactura(carrito)
                    print ("Adios")
        elif opc=="3":
            id=3
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                if vol_agregar == "si":
                    main(menu)
                elif vol_agregar != "si":
                    opc="S"
                    imprimirfactura(carrito)
                    print ("Adios")
        elif opc=="4":
            id=4
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                if vol_agregar == "si":
                    main(menu)
                elif vol_agregar != "si":
                    opc="S"
                    imprimirfactura(carrito)
                    print ("Adios")
        elif opc=="5":
            id=5
            cantidad = int(input("Cuantas lbs de arroz quieres: "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                precio_tot = 50 * cantidad
                agregar_al_carrito (id,cantidad,precio_tot)
                vol_agregar = input("¿Quieres ordenar algo mas? ")
                if vol_agregar == "si":
                    main(menu)
                elif vol_agregar != "si":
                    opc="S"
                    imprimirfactura(carrito)
                    print ("Adios")
                
main(menu)