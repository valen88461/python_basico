Nombre=input("escribe tu nombre")
Edad=int(input("escribe tu edad"))
if Edad >=60:
    print(f" {Nombre} es adulto mayor")
elif Edad >= 18:
    print (f" {Nombre} es Adulto")
elif Edad >= 12:
    print(f"{Nombre} es Adolescente")
elif Edad >=0:
    print (f"{Nombre} es Niño")
else:
    print(f"{Nombre} Edad inválida")