# module
from math import pi, cos, sin, tan, atan, sqrt
    
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
    sd = b
    x = None
    y = None
    tx = None
    ty = None
    tz = None
    if situation == 1:
        x = sensorX + x0
        y = sensorY + y0
        X = x0
        Y = y0
    elif situation == 2:
        x = sensorY + x0
        y = sensorX + y0
        X = y0
        Y = x0
    elif situation == 3:
        x = sensorX + x0
        y = -sensorY + y0
        X = x0
        Y = -y0
    elif situation == 4:
        x = sensorY + x0
        y = -sensorX + y0
        X = -y0
        Y = x0
    elif situation == 5:
        x = -sensorX + x0
        y = sensorY + y0
        X = -x0
        Y = y0
    elif situation == 6:
        x = -sensorY + x0
        y = sensorX + y0
        X = y0
        Y = -x0
    elif situation == 7:
        x = -sensorX + x0
        y = -sensorY + y0
        X = -x0
        Y = -y0
    elif situation == 8:
        x = -sensorY + x0
        y = -sensorX + y0
        X = -y0
        Y = -x0
    else:
        pass
    (ax, ay, az) = (cos(sd), -sin(sd), tan(x))
    (bx, by, bz) = (-sin(sd), -cos(sd), tan(y))
    (tx, ty, tz) = (ay*bz-by*az, bx*az-ax*bz, ax*by-bx*ay)
    return (tx, ty, tz), X, Y

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

# output: degree, direction, X, Y
def func(p1, p2, p3, p4, p5, p6, p7):
    p1 = angToRad(p1)
    p2 = angToRad(p2)
    p3 = angToRad(p3)
    p4 = angToRad(p4)
    p5 = angToRad(p5)
    returnVector, X, Y = initPara(p1, p2, p3, p4, p5, p6)
    # display X, Y
    if p7 == 2:
        print("X: ", radToAng(limitTwoPi(X)), "Y: ", radToAng(limitTwoPi(Y)))
    p = resultFinal(returnVector)
    # display degree, direction
    if p7 >= 1: 
        print('degree: ', format(radToAng(limitTwoPi(p[0])),"0.6f"),' ','direction: ',\
        format(radToAng(limitTwoPi(p[1])), "0.6f"))
    return radToAng(limitTwoPi(p[0])), radToAng(limitTwoPi(p[1])), \
        radToAng(limitTwoPi(X)), radToAng(limitTwoPi(Y))

# test func
# degree:  0.033500   direction:  69.750000
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 1, 0)
func(0, 0, c, d, 90, 1, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 2, 0)
func(0, 0, c, d, 90, 2, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 3, 0)
func(0, 0, c, d, 90, 3, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 4, 0)
func(0, 0, c, d, 90, 4, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 5, 0)
func(0, 0, c, d, 90, 5, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 6, 0)
func(0, 0, c, d, 90, 6, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 7, 0)
func(0, 0, c, d, 90, 7, 1)
a, b, c, d = func(0.0335, 69.75, 0, 0, 90, 8, 0)
func(0, 0, c, d, 90, 8, 1)

print()

# test func
"""
X:  0.0213976725811182     Y:  359.9742721127599
degree:  35.467385         direction:  191.058204
X:  359.9742721127599      Y:  0.0213976725811182
degree:  35.499740         direction:  138.844774
X:  0.0213976725811182     Y:  0.025727887240133654
degree:  35.514334         direction:  48.907744
X:  0.025727887240133654   Y:  0.0213976725811182
degree:  35.511362         direction:  101.083346
X:  359.9786023274189      Y:  359.9742721127599
degree:  35.457693         direction:  228.881930
X:  359.9742721127599      Y:  359.9786023274189
degree:  35.460667         direction:  281.126989
X:  359.9786023274189      Y:  0.025727887240133654
degree:  35.504670         direction:  11.152031
X:  0.025727887240133654   Y:  359.9786023274189
degree:  35.472318         direction:  318.944983
"""
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 1, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 2, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 3, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 4, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 5, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 6, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 7, 2)
func(0.033463180521827, 69.750018677732967, 13, 34, 120, 8, 2)
