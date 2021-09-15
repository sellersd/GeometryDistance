from random import randint as rint

def circle():
    h = rint(-20, 20)
    k = rint(-20, 20)
    r = rint(1, 20)

    while r == 0:
        r = rint(-20, 20)

    if h == 0:
        x_part = 'x^{2}'
    else:
        x_part = '(x' + sign(h) + str(h) + ')^{2}'
    if k == 0:
        y_part = 'y^{2}'
    else:
        y_part = '(y' + sign(k) + str(k) + ')^{2}'
    
        print('\\question\t$' + x_part + ' + ' +
              y_part + '=',r*r,'$')
        print('\\begin{solution}')
        print('center: (', -h, ', ', -k, ')')
        print('radius: ', r)
        print('\\end{solution}\n')

def sign(num):
    if num >= 0:
        return '+'
    else:
        return ''

for x in range(20):
    circle()

