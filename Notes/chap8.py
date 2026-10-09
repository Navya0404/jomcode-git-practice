print("\nWORKED EXAMPLE 1")
workshop = {"id": "w1", "title": "Python", "capacity": 20}
print(workshop["title"])
# title -> "Python"
print(workshop.get("venue", "TBC"))
# there is no "venue"
# so .get() uses the backup/default value:
print("title" in workshop)

print("\nWORKED EXAMPLE 2")
participant_ids = ["u2", "u1", "u2"]
unique_ids = set(participant_ids)
# set() removes duplicates
print(sorted(unique_ids))
# sorted() put the values in alphabetical order
print("u1" in unique_ids)
print(unique_ids & {"u1", "u3"})
# & means intersection

print("\nWORKED EXAMPLE 3")
workshops = [
# There are 2 workshops
    {"id": "w1", "capacity": 0},
# id = "w1"
# capacity = 0
    {"id": "w2", "capacity": 5},
# id = "w2"
# capacity = 5
]
open_ids = [row["id"] for row in workshops if row["capacity"] > 0]
print(open_ids)