import os


# Define el directorio donde están los archivos
directorio = "fotos"

# Opcional: define un prefijo o sufijo (puede estar vacío si no lo necesitas)
prefijo = "DSC_"

# Listar los archivos en el directorio
archivos = os.listdir(directorio)

numero = 1


# Renombrar los archivos
for archivo in archivos:
    # Obtén la ruta completa de los archivos
    ruta_antigua = os.path.join(directorio, archivo)

    # Extrae el nombre y extensión del archivo
    nombre, extension = os.path.splitext(archivo)

   

    # Nuevo nombre para el archivo
    nuevo_nombre = f"{prefijo}{numero}{extension}"
    ruta_nueva = os.path.join(directorio, nuevo_nombre)
    
    # Renombrar el archivo
    os.rename(ruta_antigua, ruta_nueva)
   
    print(f"{nuevo_nombre}")

    numero += 1

    

print("Renombrado completado.")
