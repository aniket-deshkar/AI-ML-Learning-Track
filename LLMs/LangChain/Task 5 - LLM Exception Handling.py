from langchain_core.tools import tool
import math

@tool
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    try:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2
    except Exception as e:
        return f"Error: {e}"

test = -5


try:
    result = calculate_circle_area.invoke({'radius': test})
    print(f"Radius {test}: {result}")
except Exception as e:
    print(f"Radius {test}: Exception - {e}")