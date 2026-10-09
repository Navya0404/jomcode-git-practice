print("\nWORKED EXAMPLE 1")
for attempt in range(1, 4):
    print(f"Attempt {attempt}")
# f = formatted string using {}
# for loop means will repeat smtg mutliple times
# start at 1, stops before 4
# attempt = 1
# attempt = 2
# attempt = 3

# output
# WORKED EXAMPLE 1
# Attempt 1
# Attempt 2
# Attempt 3

print("\nWORKED EXAMPLE 2")
total = 0
for count in [3, 5, 2]:
    total += count
print(total)

# python takes one at a time
# total += count
# total = total + count
# 0 + 3 = 3
# 3 + 5 = 8
# 8 + 2 = 10
# print(total)
# 10
# output
# WORKED EXAMPLE
# 10

print("\nWORKED EXAMPLE 3")
attempt = 0 
while attempt < 3:
    attempt += 1
    print(attempt)
print("Stopped")
# while loop keeps repeating as long as a condition is True
# 0 < 3 is true
# attempt += 1
# 0 + 1 = 1 (print attempt)
# 1
# again 1 < 3 is true 
# 1 + 1 = 2 print 2
# 2 < 3 is true print 3
# 3 < 3 is false now print stopped
# output 
# WORKED EXAMPLE 3
# 1
# 2
# 3
# Stopped