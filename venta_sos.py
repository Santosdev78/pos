import os

class Cliente:
    def __init__(self,id_sec,nombre_cliente,fecha):
        self.id_sec=id_sec
        self.nombre_cliente=nombre_cliente
        self.fecha=fecha
    def getidCliente (self):
        return self.id_sec
    def getnombreCliente (self):
        return self.nombre_cliente
    def getfecha (self):
        return self.fecha



menu=[{'id':1, 'nombre':'Arroz', 'precio':50},
    {'id':2, 'nombre':'Habichuelas', 'precio':80},
     {'id':3, 'nombre':'Aceite', 'precio':300},
     {'id':4, 'nombre':'Pollo', 'precio':85},
     {'id':5, 'nombre':'Lechuga', 'precio':80},]

carrito=[]
clientes=[]
id_sec = 0

def imprimir_menu(menu):
    tammax=0
    for item in menu:
        tamactual=len(str(item['id']))+len(item['nombre'])+len(str(item['precio']))
    if tamactual>tammax:
        tammax=tamactual
    print('-'*(int(tammax/2+2))+'Menú'+'-'*(int(tammax/2+2)))
    for item in menu:
        print(f'{item['id']}. {item['nombre']} -> RD${item['precio']}')

def buscar_producto(id,menu):
    for producto in menu:
        if producto["id"] == int(id):
            return True
    return False

def agregar_al_carrito (id,cantidad):
    ag=0
    for item in carrito:
        if item['id'] == id:
            item['cantidad'] += cantidad
            item['precio total'] = item['precio'] * item['cantidad']
            ag=1
    if ag!=1:
        if id == 1:
            carrito.append({"id": 1,"nombre":"arroz","precio":50,"cantidad":cantidad,"precio total":cantidad*50})
        elif id == 2:
            carrito.append({"id": 2,"nombre":"habichuelas","precio":80,"cantidad":cantidad,"precio total":cantidad*80})
        elif id == 3:
            carrito.append({"id": 3,"nombre":"aceite","precio":300,"cantidad":cantidad,"precio total":cantidad*300})
        elif id == 4:
            carrito.append({"id": 4,"nombre":"pollo","precio":85,"cantidad":cantidad,"precio total":cantidad*85})
        elif id == 5:
            carrito.append({"id": 5,"nombre":"lechuga","precio":80,"cantidad":cantidad,"precio total":cantidad*80})

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
    ultimo_cliente=clientes[-1]
    tamnombrecliente=1
    for cliente in clientes:
        tamnombreclienteact=len(ultimo_cliente.getnombreCliente())
        if tamnombreclienteact>tamnombrecliente:
            tamnombrecliente=tamnombreclienteact
    if tamnombrecliente-6<0:
        tamnombrecliente=1
    print((" "*2)+' '*(tamid+2)+(" "*6)+' '*(tamnombre+1)+(" "*6)+' '*(tamprecio)+(" ")+"Cliente:"+(" "*tamnombrecliente)+"ID:",ultimo_cliente.getidCliente())
    print((" "*2)+' '*(tamid+2)+(" "*6)+' '*(tamnombre+1)+(" "*6)+' '*(tamprecio),ultimo_cliente.getnombreCliente()+" "*(tamnombrecliente-8)+"Fecha: ",ultimo_cliente.getfecha())
    print('ID'+' '*(tamid+2)+'Nombre'+' '*(tamnombre+1)+'Precio'+' '*(tamprecio)+(" ")+"Cantidad"+("   ")+"Precio Total")
    for item in carrito:
        print(str(item['id'])+' '*(tamid+4-len(str(item['id'])))+item['nombre']+' '*(tamnombre+7-len(item['nombre']))+str(item['precio'])+(" "*6)+str(item["cantidad"])+(" "*10)+str(item["precio total"]))
    subtotal = 0
    for item in carrito:
        subtotal += item['precio'] * item['cantidad']
    impuestos= subtotal*0.18
    total=subtotal+impuestos
    print ((" "*2)+' '*(tamid+2)+(" "*6)+' '*(tamnombre+1)+(" "*6)+' '*(tamprecio)+(" ")+"Subtotal"+(" "*2),subtotal,"RD$")
    print ((" "*2)+' '*(tamid+2)+(" "*6)+' '*(tamnombre+1)+(" "*6)+' '*(tamprecio)+(" ")+"Impuesto"+(" "*2),impuestos,"RD$")
    print ((" "*2)+' '*(tamid+2)+(" "*6)+' '*(tamnombre+1)+(" "*6)+' '*(tamprecio)+(" ")+"Total"+(" "*5),total,"RD$")

def insertar_cliente ( nombre_cliente,fecha,clientes):
    global id_sec
    id_sec+=1
    cliente_temp=Cliente( id_sec, nombre_cliente, fecha)
    clientes.append(cliente_temp)

def main(menu):
    while True:
        os.system("cls")
        imprimir_menu(menu)
        opc=input("¿Que producto desea agregar? ")
        id = int(opc)
        encontrado=buscar_producto(id, menu)
        if encontrado==True:
            cantidad = int(input("¿Cuantas lbs quieres? "))
            if cantidad <=0:
                input ("No se puede ingresar una cantidad negativa, ni tampoco 0. Presione enter para volver al menu: ")
            else:
                agregar_al_carrito(id, cantidad)
                volver = input("¿Deseas añadir algo más?: ")
                if volver != "si":
                    nombre=input("Nombre: ")
                    fecha=input("Fecha: ")
                    insertar_cliente(nombre,fecha,clientes)
                    imprimirfactura(carrito)
                    break
        else:
            print("Producto no encontrado")
            input ("Presione ENTER para volver al menu")
main(menu)