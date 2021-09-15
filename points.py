from random import randint as rint
import math

class Point():
    def __init__(self):
        self.coords = [rint(-20, 20), rint(-20,20)]

    def toString(self):
        return '(' + str(self.coords[0]) + ', ' + str(self.coords[1]) + ')'

    def getCoords(self):
        return self.coords

def distance(p, q):
    d = math.sqrt(pow(p.coords[0] - q.coords[0],2) +
                  pow(p.coords[1] - q.coords[1],2))
    
    return round(d, 2)

def solution(p, q):
    center = p.getCoords()
    h = -center[0]
    k = -center[1]
    r = distance(p, q)
    if h == 0:
        x_part = 'x^{2}'
    else:
        x_part = '(x' + sign(h) + str(h) + ')^{2}'
    if k == 0:
        y_part = 'y^{2}'
    else:
        y_part = '(y' + sign(k) + str(k) + ')^{2}'
    
    print('\t$' + x_part + ' + ' +
           y_part + '=',round(r*r, 2),'$')

def sign(num):
    if num >= 0:
        return '+'
    else:
        return ''

print('\\uplevel{Find the distance between the points.}')
for x in range(10):
    p = Point()
    q = Point()
    
    print('\\question $', p.toString(), ', ', q.toString(), '$')
    print('\\begin{solution}')
    print(distance(p,q))
    print('\\end{solution}\n')
print('\\uplevel{Write the two equations of the circles passing through the points.}')
    
for x in range(10):
    p = Point()
    q = Point()
    print('\\question $', p.toString(), ', ', q.toString(), '$')
    print('\\begin{solution}')
    solution(p, q)
    solution(q, p)
        
    print('\\end{solution}\n')

print('\\uplevel{Is the given point inside, outside, or on the circumference of the circle.}')
for x in range(10):
    p = Point()
    q = Point()
    t = Point()

    print('\\question', end=' ')
    solution(p, q)
    print('\n$(', t.getCoords()[0], ', ', t.getCoords()[1], ')$')

