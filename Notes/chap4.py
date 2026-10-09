print("\nWORKED EXAMPLE 1")
title = "Navya"
# N a v y a
# 0 1 2 3 4
print(title[0], title [-1])
# 0- N, -1 - a
# N a
print(title[:3])
# start from the beg n stop bfr 3
# Nav
print(title[3:])
# start at positin 3 and go till end
# ya
print(title[20:])
# no position 20
# extra
# spaces also count as characters

# WORKED EXAMPLE 1
# N a
# Nav
# ya
#

print("\nWORKED EXAMPLE 2")
name = " COOKIE CRUMBS "
email = " COOCOKIECRUMB@GMAIL.COM "
print(name.strip())
# removes spaces from beg and end
# not spaces in btw
print(email.strip().lower())
# remove space both ends
# make the character lower case

#output
# WORKED EXAMPLE 2
# COOKIE CRUMBS
# coocookiecrumb@gmail.com

print("\nWORKED EXAMPLE 3")
capacity_text = input("Capacity: ")
# input from user
# capacity_text = "20"
registered_text = input("Registered: ")
# input from user
# registered_text = "7"
capacity = int(capacity_text)
registered = int(registered_text)
print(f"Remaining: {capacity - registered}")
# 20 - 7 = 13

# output
# WORKED EXAMPLE 3
# Capacity: 20
# Registered: 7
# Remaining: 13