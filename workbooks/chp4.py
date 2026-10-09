print("\nWORKED EXAMPLE 1")
title = "Navya"
print(title[0], title [-1])
print(title[:3])
print(title[3:])
print(title[20:])

print("\nWORKED EXAMPLE 2")
name = " COOKIE CRUMBS "
email = " COOCOKIECRUMB@GMAIL.COM "
print(name.strip())
print(email.strip().lower())

print("\nWORKED EXAMPLE 3")
capacity_text = input("Capacity: ")
registered_text = input("Registered: ")
capacity = int(capacity_text)
registered = int(registered_text)
print(f"Remaining: {capacity - registered}")