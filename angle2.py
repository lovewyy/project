# module
from math import pi, cos, sin, tan, atan, sqrt

# define cot
def cot(rad: 'double') -> 'double':
    return 1 / tan(rad)
    
# test for cot
# print(cot(pi / 4) - 1.0 < 0.000001)

# helper function
# transform angle to rad 
def angToRad(ang: 'double') -> 'double':
    return pi / 180 * ang

# transform rad to angle
def radToAng(rad: 'double') -> 'double':
    return 180 / pi * rad

# limit in [0, 2*pi)
def limitTwoPi(rad: 'double') -> 'double':
    while rad >= 2 * pi:
        rad -= 2 * pi
    while rad < 0:
        rad += 2 * pi
    return rad

# step1: init
def initPara(initDegree: 'double', initPosition: 'double' , \
        sensorX: 'double', sensorY: 'double', sensorPosition: 'double', situation: int):
    """
    initDegree: t(heta)
    initPosition: a(lpha)
    sensorX: x  set 0
    sensorY: y  set 0
    sensorPosition: b(eta)
    situation: s
    return: Transformed for step2
    """
    # rename parameters according to doc
    t = initDegree
    a = initPosition
    b = sensorPosition
    x0 = atan(cos(a-b)*tan(t))
    y0 = atan(sin(a-b)*tan(t))
    print("x: ", radToAng(limitTwoPi(x0)), "y: ", radToAng(limitTwoPi(y0)))
    x = sensorX + x0
    y = sensorY + y0
    sd = b
    if situation == 1:
        (ax, ay, az) = (cos(sd), -sin(sd), tan(x))
        (bx, by, bz) = (-sin(sd), -cos(sd), tan(y))
        (tx, ty, tz) = (ay*bz-by*az, bx*az-ax*bz, ax*by-bx*ay)
        return (tx, ty, tz)
    
# step2: return (degree, direction)
def resultFinal(para: 'tuple')  -> 'tuple':
    (x, y, z) = para 
    angle = 0
    direction = None
    if z > 0:
        angle = atan(sqrt(x * x + y * y) / abs(z))
        if y > 0:
            direction = pi / 2 + atan(x / y)
        elif y < 0:
            direction = 3 * pi / 2 + atan(x / y)
        else:
            if x > 0:
                direction = pi
            elif x < 0:
                direction = 0.0
            else:
                pass
    elif z < 0:
        angle = atan(sqrt(x * x + y * y) / abs(z))
        if y > 0:
            direction = 0 - pi / 2 + atan(x / y)
        elif y < 0:
            direction = pi / 2 + atan(x / y)
        else:
            if x > 0:
                direction = 0.0 
            elif x < 0:
                direction = pi
            else:
                pass
    else:
        pass
    return (angle, direction)

def func(p1, p2, p3, p4, p5, p6):
    p1 = angToRad(p1)
    p2 = angToRad(p2)
    p3 = angToRad(p3)
    p4 = angToRad(p4)
    p5 = angToRad(p5)
    returnVector = initPara(p1, p2, p3, p4, p5, p6)
    p = resultFinal(returnVector)
    print('degree: ', format(radToAng(limitTwoPi(p[0])),"0.6f"),' ','direction: ',\
        format((radToAng(limitTwoPi(p[1]))), "0.6f"))

# func(0, 0, -0.00666, -0.00166, 20, 1)
func(10, 135, 0, 0, 90, 1)
func(10, 135, 45, 45, 90, 1)
