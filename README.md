# 🍕 Pizza Decorator Pattern — Python

A clean Python implementation of the **Decorator Design Pattern** using a pizza topping example, with ABC-enforced interfaces.

---

## 📌 What is the Decorator Pattern?

The **Decorator Pattern** is a structural design pattern that lets you **dynamically add behavior to an object** without modifying its original class or using inheritance chains.

Instead of creating subclasses like `CheeseTomatoPizza`, `CheesePizza`, `TomatoOnionPizza` (which explodes combinatorially), decorators **wrap** objects and extend them one layer at a time.

---

## 🗂️ Project Structure

```
pizza_decorator/
│
├── interfaces/
│   └── ipizza.py           # Abstract base interface (ABC)
│
├── pizza/
│   └── pizza.py            # Concrete base pizza
│
├── decorators/
│   ├── pizza_decorator.py  # Base decorator (wraps IPizza)
│   ├── cheese_decorator.py
│   ├── tomato_decorator.py
│   └── onion_decorator.py
│
└── main.py                 # Client code
```

---

## 🧱 Class Breakdown

| Class | Role |
|---|---|
| `IPizza` | Abstract interface — enforces `get_pizza_type()` |
| `Pizza` | Concrete base object |
| `PizzaDecorator` | Base decorator — wraps any `IPizza` |
| `CheeseDecorator` | Adds `"with extra cheese"` |
| `TomatoDecorator` | Adds `"with extra tomatoes"` |
| `OnionDecorator` | Adds `"with extra onion"` |

---

## ➕ Adding a New Topping

Just create a new decorator — no existing code needs to change:

```python
class MushroomDecorator(PizzaDecorator):
    def get_pizza_type(self):
        return super().get_pizza_type() + "\nwith extra mushrooms"
```

Then use it:

```python
pizza = MushroomDecorator(pizza)
```

This follows the **Open/Closed Principle** — open for extension, closed for modification.

---

## 🧠 Key OOP Concepts Used

- **Abstraction** — `IPizza` defines the contract via `ABC`
- **Inheritance** — decorators extend `PizzaDecorator`
- **Composition** — each decorator holds a reference to another `IPizza`
- **Polymorphism** — all decorators are interchangeable as `IPizza` objects

---

## 🐍 Requirements

- Python 3.x
- No external libraries needed

---

## 👤 Author

**Muhammad Abdullah**  
