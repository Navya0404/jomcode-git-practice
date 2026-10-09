print("\nWORKED EXAMPLE 1")
titles = ["Python"]
titles.append("Web")
titles.extend(["SQL", "React"])
removed = titles.pop()
print(titles)
print(removed)

print("\nWORKED EXAMPLE 2")
dimensions = (1280, 720)
width, height = dimensions
print(width, height)
print(dimensions[:1])

print("\nWORKED EXAMPLE 3")
original = ["Python"]
alias = original
copy = original.copy()
alias.append("SQL")
print(original)
print(copy)