print("\nWORKED EXAMPLE 1")
import math
from pathlib import Path

print(math.ceil(4.2))
print(Path("backend") / "app" / "main.py")

print("\nWORKED EXAMPLE 2")
import json

records = [{"title": "Python", "capacity": 20}]
text = json.dumps(records, indent=2)
restored = json.loads(text)
print(restored == records)
print(restored[0]["capacity"])

print("\nWORKED EXAMPLE 3")
import os

def api_origin():
    return os.getenv("API_ORIGIN", "http://localhost:8000")

print(api_origin())