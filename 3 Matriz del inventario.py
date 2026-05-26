# Matriz del inventario
inventario = [
    [101, "Cuadernos", 3, 10],
    [102, "Lapices", 15, 10],
    [103, "Borradores", 2, 5],
    [104, "Marcadores", 8, 12],
    [105, "Colores", 20, 15]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar lista de pedidos
print("LISTA DE PEDIDOS\n")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)
    print("-----------------------------")