print("\nWORKED EXAMPLE 1")
workshop = {"id": "w1", "title": "Python", "capacity": 20}
print(workshop["title"])
print(workshop.get("venue", "TBC"))
print("title" in workshop)

print("\nWORKED EXAMPLE 2")
participant_ids = ["u2", "u1", "u2"]
unique_ids = set(participant_ids)
print(sorted(unique_ids))
print("u1" in unique_ids)
print(unique_ids & {"u1", "u3"} )

print("\nWORKED EXAMPLE 3")
workshops = [
    {"id": "w1", "capacity": 0},
    {"id": "w2", "capacity": 5},
]
open_ids = [row["id"] for row in workshops if row["capacity"] > 0]
print(open_ids)
