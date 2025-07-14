productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(marca):
    marca = marca.lower()
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower()==marca:
            encontrados = True
            if modelo in stock:
                print(f"Modelo: {modelo} - Stock: {stock[modelo][1]}")
            else:
                print(f"Modelo: {modelo} - Stock: No disponible")
        if not encontrados:
            print("No hay productos de esa marca.")

def buesqueda_precio(p_min, p_max):
    resultados = []
    for modelo , info in stock.items():
        precio, cantidad = info
        if p_min <= precio <= p_max and cantidad > 0:
            if modelo in productos:
                marca = productos[modelo][0]
                resultados.append(f"{marca}--{modelo}")
    if resultados:
        resultados.sort()
        for item in resultados:
            print(item)
    else:
        print("No hay notebooks en ese rango de precios")

def Actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    return False

def main():
    while True:
        print("\n---MENU DE OPCIONES---")
        print("1. Stock Marca")
        print("2. Busqueda por precio")
        print("3. Actualizar Precio")
        print("4. Salir")

def main():
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        marca = input("Ingrese la marca que desea: ")
        stock_marca(marca)

    elif opcion == "2":
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese el precio maximo: "))
                break
            
            except ValueError:
                print("Precio Invalido Debe Ingresar valores enteros")
            buesqueda_precio(p_min, p_max)

    elif opcion == "3":
        while True: 
            modelo = input("Ingrese modelo a actualizar: ")
            try:
                nuevo_precio = int(input("Ingrese el precio nuevo"))
            
            except ValueError: 
                print("Debe ingresar un precio valido")
            continue

    resultado = Actualizar_precio(modelo, nuevo_precio)
    if resultado:
        print("Precio actualizado")
    else:
        print("modelo no existe")

    seguir = input("¿Desea seguir?")
    if seguir  != "Si":
        break

    elif opcion == "4":
        print("Programa Finalizado")
        break

    else:
        print("Debe seleccionar una opcion valida")

if _name_ == "__main__":
    main()

            
                




    
    
    
     


