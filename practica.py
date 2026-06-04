#Mostrar un mensaje de bienvenida.
#Solicitar al usuario cuántos productos desea registrar.
#Registrar todos los productos que el usuario indique.
#Guardar los productos en una lista.
#Mostrar todos los productos registrados.
#Mostrar el número total de productos registrados.
#Si el total de productos es menor a 5 mostrar:
print("=====Bienvenido a guarda tus productos=======")
productos=[]
contador=0
productos_registrados=int(input("¿Cuantos productos desea registrar?: "))
for producto in range (productos_registrados):
    productos_usuario=input("escribe el nombre del producto: ")
    productos.append(productos_usuario)
    contador+=1
print("========resumen=============")
print(f" producto {contador} = {productos} ")
print(f"numero total de productos registrados =  {contador} ")
if contador<5:
    print("Inventario pequeño")
else:
    print("Inventario suficiente")    