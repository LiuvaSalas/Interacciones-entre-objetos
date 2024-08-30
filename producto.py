class Producto:
    """Clase que representa un producto."""

    def __init__(self, nombre, precio, stock=0):
        """Inicializa un nuevo producto.

        Parametros:
            nombre: str, El nombre del producto.
            precio: float, El precio del producto.
            stock: int, La cantidad en stock del producto.
        """
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        """str: El nombre del producto."""
        return self.__nombre

    @property
    def precio(self):
        """float: El precio del producto."""
        return self.__precio

    @property
    def stock(self):
        """int: La cantidad en stock del producto."""
        return self.__stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("El stock no puede ser negativo")
        self.__stock = value

    def __eq__(self, other):
        """Compara si dos productos son iguales por nombre, ignorando mayúsculas y minúsculas."""
        return self.nombre.lower() == other.nombre.lower()

    def __add__(self, other):
        """Suma la cantidad en stock de dos productos si tienen el mismo nombre."""
        if self == other:
            return Producto(self.nombre, self.precio, self.stock + other.stock)
        else:
            return None

    def __sub__(self, other):
        """Resta la cantidad en stock de un producto de otro si tienen el mismo nombre."""
        if self == other:
            if self.stock >= other.stock:
                return other.stock
            else:
                return self.stock
        else:
            return 0

    def __str__(self):
        """Representación de cadena del producto."""
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"