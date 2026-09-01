Nombre=input("escribe tu nombre: ")
Contraseña=input("escribe tu contraseña: ")
Esta_registrado=input("¿esta registrado:? ")
su_cuenta_es_activa=input("¿su cuenta esta activa?:  ")
if   Contraseña == "AgroRed2026"and Esta_registrado =="si" and su_cuenta_es_activa =="si":
    print(f"{Nombre} acceso permitido.")
else:
    print(f"{Nombre}, acceso denegado.")