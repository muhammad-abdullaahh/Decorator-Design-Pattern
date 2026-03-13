from decorators.pizza_decorator import PizzaDecorator

class TomatoDecorator(PizzaDecorator):
    """Adds extra tomatoes to the pizza."""
    def get_pizza_type(self):
        return super().get_pizza_type() + "\nwith extra tomatoes"