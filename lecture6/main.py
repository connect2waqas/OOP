class Point:
    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
    def __str__(self):
        return f"<{self.x_cord},{self.y_cord}>"
    
    def euclidean_distance(self,other):
        return ((self.x_cord - other.x_cord) **2 + (self.y_cord - other.y_cord)**2) **0.5
    
    def distance_from_orgin(self):
        return self.euclidean_distance(Point(0,0))
        # return ((self.x_cord)**2 + (self.y_cord) **2) **0.5


class Line:
    
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    
    def point_on_line(line,point):
        if line.A * point.x_cord + line.B * point.y_cord + line.C == 0:
            return "Lie on line"
        else:
            return "Does not lie on line"
        
    def shortest_distance(line, point):
        return abs(line.A*point.x_cord + line.B * point.y_cord + line.C)/ (line.A**2 + line.B**2) ** 0.5
        
l1 = Line(1,1,-2)
p1 = Point(1,1)
print(l1)
print(p1)
print(l1.shortest_distance(p1))