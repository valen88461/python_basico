nombre=input("escriba su nombre: ")
Usuario_registrado=input("¿es un usuario registrado? si/no:")
publicacion_activa=input("¿la publicacion esta activa? si/no:")
administrador=input("¿es administrador?: si/no: ")
if(Usuario_registrado == 'si' and publicacion_activa == "si" ) or administrador== 'si':
  print(f'{nombre}, puede contactar al vendedor')
  
else:
    print(f'{nombre}, no puede contactar al vendedor.')