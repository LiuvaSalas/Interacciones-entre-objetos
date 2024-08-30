from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    """Clase abstracta que representa una tienda."""

    def __init__(self, nombre, costo_delivery):
        """Inicializa una nueva tienda.

        Parametros:
            - nombre: str, el nombre de la tienda.
            - costo_delivery: float, el costo de delivery de la tienda.
            - productos: list, genera una lista vacia para cada tienda al momento de crearla.
        """
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        """str: El nombre de la tienda."""
        return self.__nombre

    @property
    def costo_delivery(self):
        """float: El costo de delivery de la tienda."""
        return self.__costo_delivery

    @property
    def productos(self):
        """list: Lista de productos de la tienda."""
        return self.__productos

    @abstractmethod
    def ingresar_producto(self, producto):
        """Metodo abstracto para ingresar un producto a la tienda."""
        pass

    @abstractmethod
    def listar_productos(self):
        """Metodo abstracto para listar los productos de la tienda."""
        pass

    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        """Metodo abstracto para realizar una venta en la tienda."""
        pass

class Restaurante(Tienda):
    """Clase que representa un restaurante."""

    def ingresar_producto(self, producto):
        """Metodo para ingresar un producto al restaurante.

        Parametros:
            - producto: list, genera una lista con los productos y su stock al momento del usuario ingresarlos.
        """        
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  # Sumar el stock si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Metodo para listar los productos del restaurante.

        Parametros:
            - tipo_tienda: int, id de tienda especifico

        Return:
            - resultado: str, texto con resumen del producto y precio.
        """
        if tipo_tienda == 3:
            resultado = "\n".join([f"{producto.nombre} - ${producto.precio}" for producto in self.productos])
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Metodo para realizar una venta en el restaurante.

        Parametros:
            - nombre_producto: str, nombre del producto a vender
            - cantidad: int, cantidad de producto que el usuario desea comprar.

        Return:
            - str, con la venta del producto, cantidad y el nombre del producto.
        """
        for p in self.productos:
            if p.nombre == nombre_producto:
                print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                break
        else:
            print("El producto solicitado no está disponible")

class Supermercado(Tienda):
    """Clase que representa un supermercado."""

    def ingresar_producto(self, producto):
        """Metodo para ingresar un producto al supermercado.

        Parametros:
            - producto: list, genera una lista con los productos y su stock al momento del usuario ingresarlos.
        """
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  #suma el stock ingresado en la segunda vuelta si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Metodo para listar los productos del supermercado.

        Parametros:
            - tipo_tienda: int, id de tienda especifico

        Return:
            - resultado: str, texto con resumen del producto y precio,
            y un mensaje en especifico si el stock del producto listado
            es menor a 10.
        """
        if tipo_tienda == 2:
            resultado = "\n".join(
                [f"{producto.nombre} - Stock: {producto.stock}{' - Pocos productos disponibles' if producto.stock < 10 else ''} - ${producto.precio}" for producto in self.productos]
            )
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Metodo para realizar una venta en el supermercado.

        Parametros:
            - nombre_producto: str, nombre del producto a vender
            - cantidad: int, cantidad de producto que el usuario desea comprar.

        Return:
            - str, con la venta del producto, cantidad, el nombre del producto,
            y el stock actualizado luego de comprar.
        """
        for p in self.productos:
            if p.nombre == nombre_producto:
                print("---------stock inicial")
                print(p.stock)
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                    print("---------stock final")
                    print(p.stock)
                else:
                    print("No hay suficiente stock para realizar la venta")
                break
        else:
            print("El producto solicitado no está disponible")

class Farmacia(Tienda):
    """Clase que representa una farmacia."""
    

    def ingresar_producto(self, producto):
        """Metodo para ingresar un producto a la farmacia.

        Parametros:
            - producto: list, genera una lista con los productos y
            su stock al momento del usuario ingresarlos.
        """
        for p in self.productos:
            if p == producto:
                p.stock += producto.stock  # Sumar el stock si el producto ya existe
                break
        else:
            self.productos.append(producto)

    def listar_productos(self, tipo_tienda: int):
        """Metodo para listar los productos de la farmacia.

        Parametros:
            - tipo_tienda: int, id de tienda especifico

        Return:
            - resultado: str, texto con resumen del producto, precio,
            y un mensaje en especifico si el valor del producto listado
            es mayor a 15000 pesos.
        """
        if tipo_tienda == 1:
            resultado = "\n".join(
                [f"{producto.nombre} - ${producto.precio}{' - Envío gratis al solicitar este producto' if producto.precio > 15000 else ''}" for producto in self.productos]
            )
            return resultado

    def realizar_venta(self, nombre_producto, cantidad):
        """Metodo para realizar una venta en la farmacia.

        Parametros:
            - nombre_producto: str, nombre del producto a vender
            - cantidad: int, cantidad de producto que el usuario desea comprar.

        Return:
            - str, con la venta del producto, cantidad, el nombre del producto,
            - str, con mensaje de stock insuficiente si la cantidad es mayor al stock
            disponible, vende lo disponible, y establece stock en 0.
        """
        for p in self.productos:
            if p.nombre == nombre_producto:
                if cantidad > 3:
                    print("No se puede solicitar más de 3 unidades por venta en una farmacia")
                    return
                if p.stock >= cantidad:
                    p.stock -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {nombre_producto}")
                else:
                    print(f"Stock insuficiente. Solo se venderán {p.stock} unidades de {nombre_producto}.")
                    p.stock = 0
                return
        print("El producto solicitado no está disponible")