from decorators.pizza_decorator import PizzaDecorator

class CheeseDecorator(PizzaDecorator):
    """Adds extra cheese to the pizza."""
    def get_pizza_type(self):
        return super().get_pizza_type() + "\nwith extra cheese"