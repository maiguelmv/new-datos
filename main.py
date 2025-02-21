import csv
import os

# Archivos CSV
CLIENTES_FILE = 'clientes.csv'
PEDIDOS_FILE = 'pedidos.csv'
INDEX_FILE = 'index.csv'

# Función para verificar si los archivos existen

def inicializar_archivos():
    if not os.path.exists(CLIENTES_FILE):
        with open(CLIENTES_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id_cliente', 'nombre', 'apellido', 'telefono', 'activo'])
    if not os.path.exists(PEDIDOS_FILE):
        with open(PEDIDOS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id_pedido', 'id_cliente', 'producto', 'precio', 'cantidad', 'activo'])

# Función para obtener el último ID usado
def obtener_nuevo_id(archivo, columna_id):
    try:
        with open(archivo, 'r') as file:
            reader = csv.DictReader(file)
            ids = [int(row[columna_id]) for row in reader]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

# Registrar un cliente
def registrar_cliente():
    id_cliente = obtener_nuevo_id(CLIENTES_FILE, 'id_cliente')
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el número de teléfono: ")
    
    with open(CLIENTES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_cliente, nombre, apellido, telefono, 1])
    print(f"Cliente {nombre} {apellido} registrado exitosamente.")

# Listar clientes
def listar_clientes():
    with open(CLIENTES_FILE, 'r') as file:
        reader = csv.DictReader(file)
        print("Clientes registrados:")
        for row in reader:
            if row['activo'] == '1':
                print(f"ID: {row['id_cliente']} | Nombre: {row['nombre']} {row['apellido']} | Tel: {row['telefono']}")

# Eliminar cliente (lógico)
def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    filas = []
    encontrado = False
    
    with open(CLIENTES_FILE, 'r') as file:
        reader = csv.reader(file)
        filas = list(reader)
    
    for fila in filas:
        if fila[0] == id_cliente:
            fila[4] = '0'
            encontrado = True
            break
    
    if encontrado:
        with open(CLIENTES_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filas)
        print("Cliente eliminado lógicamente.")
    else:
        print("Cliente no encontrado.")

# Registrar pedido
def registrar_pedido():
    id_cliente = input("Ingrese el ID del cliente que realiza el pedido: ")
    producto = input("Ingrese el producto de maquillaje: ")
    precio = input("Ingrese el precio (opcional, presione Enter para omitir): ")
    cantidad = input("Ingrese la cantidad (opcional, presione Enter para omitir): ")
    
    precio = precio if precio else 'N/A'
    cantidad = cantidad if cantidad else 'N/A'
    id_pedido = obtener_nuevo_id(PEDIDOS_FILE, 'id_pedido')
    
    with open(PEDIDOS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_pedido, id_cliente, producto, precio, cantidad, 1])
    print(f"Pedido {id_pedido} registrado exitosamente para el cliente {id_cliente}.")

# Listar pedidos de un cliente
def listar_pedidos():
    id_cliente = input("Ingrese el ID del cliente para ver sus pedidos: ")
    with open(PEDIDOS_FILE, 'r') as file:
        reader = csv.DictReader(file)
        print(f"Pedidos del cliente {id_cliente}:")
        for row in reader:
            if row['id_cliente'] == id_cliente and row['activo'] == '1':
                print(f"ID Pedido: {row['id_pedido']} | Producto: {row['producto']} | Precio: {row['precio']} | Cantidad: {row['cantidad']}")

# Eliminar pedido (lógico)
def eliminar_pedido():
    id_pedido = input("Ingrese el ID del pedido a eliminar: ")
    filas = []
    encontrado = False
    
    with open(PEDIDOS_FILE, 'r') as file:
        reader = csv.reader(file)
        filas = list(reader)
    
    for fila in filas:
        if fila[0] == id_pedido:
            fila[5] = '0'
            encontrado = True
            break
    
    if encontrado:
        with open(PEDIDOS_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(filas)
        print("Pedido eliminado lógicamente.")
    else:
        print("Pedido no encontrado.")

# Menú principal
def menu():
    inicializar_archivos()
    while True:
        print("\n--- Menú ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Registrar pedido")
        print("5. Listar pedidos de un cliente")
        print("6. Eliminar pedido")
        print("7. Salir")
        
        opcion = input("Ingrese la opción deseada: ")
        
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            eliminar_cliente()
        elif opcion == '4':
            registrar_pedido()
        elif opcion == '5':
            listar_pedidos()
        elif opcion == '6':
            eliminar_pedido()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
