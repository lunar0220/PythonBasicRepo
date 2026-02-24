import math

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> Vector2D:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2D') -> Vector2D:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self) -> float:
        return f"Vector2D({self.x}, {self.y})"