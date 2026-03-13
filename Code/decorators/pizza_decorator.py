from interfaces.ipizza import IPizza

class PizzaDecorator(IPizza):
    """Base decorator — wraps any IPizza object."""
    def __init__(self, pizza):
        self._pizza = pizza

    def get_pizza_type(self):
        return self._pizza.get_pizza_type()