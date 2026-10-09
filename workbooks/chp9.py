print("\nWORKED EXAMPLE 1")
def remaining(capacity, registered):
    return capacity - registered

value = remaining(20, 8)
print(value)
print(remaining(registered=3, capacity=5))

print("\nWORKED EXAMPLE 2")
def greeting(name, prefix="Hello"):
    return f"{prefix}, {name}"

print(greeting("Navya"))
print(greeting("Navya", prefix="Welcome"))

print("\nWORKED EXAMPLE 3")
def add_title(title, titles=None):
    if titles is None:
        titles = []
    return [*title, title]

print(add_title("Python"))
print(add_title("SQL"))
print(add_title("React", ["Python"]))

                  