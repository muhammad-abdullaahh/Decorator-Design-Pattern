from interfaces.ipizza import IPizza

class Pizza(IPizza):
    """Basic/concrete pizza implementation."""
    def get_pizza_type(self):
        return "This is normal pizza"