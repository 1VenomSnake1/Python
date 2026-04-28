'''
T1 — Rectangle (Прямоугольник)
T2 — Quad (Квадрат)
is_intersect, compare
'''
from traceback import print_tb


class Rectangle:
    def __init__(self, id_str, x, y, width, height):
        self.id = id_str
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return self.width*self.height


class Quad:
    def __init__(self, id_str, x, y, width):
        self.id = id_str
        self.x = x
        self.y = y
        self.width = width

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        return self.width*self.width


def compare(fig1, fig2):
    area1 = fig1.area()
    area2 = fig2.area()
    if area1 < area2: return -1
    elif area1 > area2: return 1
    else: return 0

def is_intersect(rect, quad):
    return not (rect.x + rect.width < quad.x or quad.x + quad.width < rect.x or
                rect.y + rect.height < quad.y or quad.y + quad.width < rect.y)

print("Программа для сравнения площадей прямоугольника и квадрата, которые заданы с помощью "
      "якорьной точки (x,y) слева-внизу, шириной и высота. "
      "Ввод производится сперва прямоугольника, затем квадрата в формате: "
      "(id фигуры, x, y, ширина, высота) у квадарат только ширина")

print("Фигура прямоугольник: ")
id = str(input("Введите id: "))
x = float(input("Введите x: "))
y = float(input("Введите y: "))
width = float(input("Введите ширину: "))
height = float(input("Введите высоту: "))

CoolRect = Rectangle(id, x, y, width, height)

print("Фигура квадрат: ")
id = str(input("Введите id: "))
x = float(input("Введите x: "))
y = float(input("Введите y: "))
width = float(input("Введите ширину: "))

CoolQuad = Quad(id, x, y, width)

if(compare(CoolRect, CoolQuad) == -1): print("Прямоугольник > Квадрата")
elif(compare(CoolRect, CoolQuad) == 1): print("Прямоугольник < Квадрата")
elif(compare(CoolRect, CoolQuad) == 0): print("Прямоугольник = Квадрата")

if(is_intersect(CoolRect,CoolQuad) == 1)