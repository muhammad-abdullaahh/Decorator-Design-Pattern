from decorators.pizza_decorator import PizzaDecorator

class OnionDecorator(PizzaDecorator):
    """Adds extra onions to the pizza."""
    def get_pizza_type(self):
        return super().get_pizza_type() + "\nwith extra onion"