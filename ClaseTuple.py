print(""" \n ---------Datos de usuario--------- \n """)
Nombre = input("Ingrese su nombre: ")
Edad = int(input("Ingrese su edad: "))

print(""" \n ---------Direcciones de usuario--------- \n """)
Direccion1 = input("Ingrese direccion de residencia 1: ")
Direccion2 = input("Ingrese direccion de residencia 2: ")

print(""" \n ---------Estudios de usuario--------- \n """)
school = input("Ingrese colegio en el que estudio: : ")
university = input("Ingrese universidad en el que estudio: : ")

print(""" \n ---------Experiencia de usuario--------- \n """)
area = input("Ingrese en que area tiene experiencia: ")
experience = int(input("Ingrese sus años de experiencia: "))


userInfo = tuple((Nombre, Edad))
userDirecciones = tuple((Direccion1, Direccion2))
userEducation = tuple((school, university))
userExperience = tuple((area, experience))

print(f"""
Usuario: {userInfo}
Direcciones: {userDirecciones}
Educacion: {userEducation}
Experiencia :{userExperience}
""")
