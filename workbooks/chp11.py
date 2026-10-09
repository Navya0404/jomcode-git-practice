print("\nWORKED EXAMPLE 1")
text = "twenty"
try:
    capacity = int(text)
except ValueError:
    print("Enter a whole number")
else:
    print(capacity)

print("\nWORKED EXAMPLE 2")
def valid_capacity(value):
    if type(value) is not int or not 1 <= value <= 500:
        raise ValueError("Capacity must be an integer from 1 to 500")
    return value

print(valid_capacity(20))

print("\nWORKED EXAMPLE 3")
import logging

logger = logging.getLogger("workshop_hub")
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
workshop_id = "w1" 
logger.info("Workshop update rejected: id=%s reason=capacity", workshop_id)