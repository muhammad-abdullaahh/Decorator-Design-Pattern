from pizza.pizza import Pizza
from decorators.cheese_decorator import CheeseDecorator
from decorators.tomato_decorator import TomatoDecorator
from decorators.onion_decorator import OnionDecorator

if __name__ == "__main__":
    pizza = Pizza()
    pizza = CheeseDecorator(pizza)
    pizza = TomatoDecorator(pizza)
    pizza = OnionDecorator(pizza)

    print("Pizza Description:")
    print("------------------")
    print(pizza.get_pizza_type())
