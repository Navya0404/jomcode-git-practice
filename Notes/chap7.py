print("\nWORKED EXAMPLE 1")
titles = ["Python"]
titles.append("Web")
# append() adds one time to the end
# ["Python", "Web"]
titles.extend(["SQL", "React"])
# extend() adds multiple items to the list
# ["Python", "Web", "SQL", "React"]
removed = titles.pop()
# pop() removes the last item from the list
print(titles)
print(removed)
# output
# ['Python', 'Web', 'SQL']
# React

print("\nWORKED EXAMPLE 2")
dimensions = (1280, 720)
# create tuple
# tupler similar to a list, but it uses ()
# 1280 - width
# 720 - height
width, height = dimensions
print(width, height)
# it will print 1280 720
# next slice
#                0    1
print(dimensions[:1])
# start from beg n stop bfr position 1
# dimensions[0] # 1280
# dimensions[:1] # (1280,)
# output
# WORKED EXAMPLE 2
# 1280 720
# (1280,)

print("\nWORKED EXAMPLE 3")
original = ["Python"]
alias = original
# this does NOT create a new list
# both variable point the same list
copy = original.copy()

alias.append("SQL")
print(original)
print(copy)

# i dont understand, later