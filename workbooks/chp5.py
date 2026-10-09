print("\nWORKED EXAMPLE 1")
capacity = 40
if 1 <= capacity <= 700:
    print("Valid capacity")
else:
    print("Capacity must be 1 to 700")

print("\nWORKED EXAMPLE 1.1")
capacity = 300
if 1 <= capacity <= 200:
    print("Valid capacity")
else:
    print("Capacity must be 1 to 20")

print("\nWORKED EXAMPLE 2")
role= "organizer"
owner_id = "u1"
current_user_id = "u2"
if role == "organizer" and owner_id == current_user_id:
    print("Can edit")
else:
    print("Forbidden")


print("\nWORKED EXAMPLE 3")
value = 0
print(value is None)
print(not value)
optional = None
print(optional is None)
