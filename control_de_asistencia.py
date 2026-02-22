presentes = []
ausentes = []
print("#----------------------------------------#")
print("#--| sistema de control de asistencia |--#")
print("#----------------------------------------#")
print("ingrese los nombres de las personas, escriba 'fin' para terminar.\n")
while True:
    nombre = input("nombre de la persona: ").strip()
    if nombre.lower() == "fin":
        break
    if nombre == "":
        print("entrada vacia, por favor ingrese un nombre valido.")
        continue
    estado = input(f"¿{nombre} esta presente? (s/n): ").lower()
    if estado == "s":
        presentes.append(nombre)
    elif estado == "n":
        ausentes.append(nombre)
    else:
        print("opcion invalida, ingrese 's' para presente o 'n' para ausente.")
print("\nlista de asistencia")
print(f"presentes ({len(presentes)}): {presentes}")
print(f"ausentes ({len(ausentes)}): {ausentes}")