class TriangleChecker:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.sides = (a, b, c)
    def is_triangle(self):
        if not all(isinstance(x,(int,float)) for x in self.sides):
            return "Только числа!"
        if any(x <=0 for x in self.sides):
            return "С отриц. числами не выйдет!"
        if self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a:
            return "Ура!"
        return "Жаль"
t= TriangleChecker(2,4,5)
print(t.is_triangle())