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

# situation error in step1
class TestException(Exception):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg
 
    def __str__(self):
        return self.msg

# test for helper function
# print(angToRad(180) == pi,radToAng(pi) == 180 )
# print(limitTwoPi(5 * pi) == pi, limitTwoPi(4 * pi) == 0)

# core function
# step1: init
def initPara(initDegree: 'double', initPosition: 'double' , \
        sensorX: 'double', sensorY: 'double', sensorPosition: 'double', situation: int):
    """
    initDegree: t(heta)
    initPosition: a(lpha)
    sensorX: x
    sensorY: y 
    sensorPosition: b(eta)
    situation: s
    return: Transformed for step2
    """
    # rename parameters according to doc
    t = initDegree
    a = initPosition
    x = sensorX
    y = sensorY
    b = sensorPosition
    s = situation
    
    # init parameters
    # if t(initDegree) equal to 0, ignore t 
    if t != 0.0:
        para1 = a 
        para2 = t 
    else:
        para1 = None
        para2 = None
    
    # different situations
    # situation 1: radial direction: x, from x to y: clockwise 
    if situation == 1:
        if x > 0:
            para3 = limitTwoPi(b)
            para4 = x
        elif x < 0:
            para3 = limitTwoPi(b + pi)
            para4 = 0 - x
        else:
            para3 = None
            para4 = None
        if y > 0:
            para5 = limitTwoPi(b + pi / 2)
            para6 = y
        elif y < 0:
            para5 = limitTwoPi(b - pi / 2)
            para6 = 0 - y
        else:
            para5 = None
            para6 = None
        
    # situation 2: radial direction: x, from x to y: clockwise 
    elif situation == 2:
        pass
    # situation 3: radial direction: x, from x to y: clockwise 
    elif situation == 3:
        pass
    # situation 4: radial direction: x, from x to y: clockwise 
    elif situation == 4:
        pass
    # other: raise error
    else:
        raise TestException('do not have the situation')
    return (para1, para2, para3, para4, para5, para6)

# test for step1
# testInit = initPara(1, 2, 3, 4, 5, 1)
# print('para: ', testInit)

# step2: return (x, y, z)
def resultVector(para: 'tuple') -> 'tuple':
    (p1, p2, p3, p4, p5, p6) = para
    a = [p1, p3, p5]
    b = [p2, p4, p6]
    x = 0
    y = 0
    z = 0
    for i in a:
        if i != None:
            x += -cos(i)
            y += sin(i)
    for j in b:
        if i != None:
            z += cot(i)
    return (x, y, z)

# test for step2
# testResultVector = resultVector(testInit)
# print('(x, y, z): ',testResultVector)

# step3: return (degree, direction)
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

# test for final
# testResultFinal = resultFinal(testResultVector)
# print('(degree, direction): ', testResultFinal)

# print result
def func(para: 'tuple') -> 'tuple':
    (p1, p2, p3, p4, p5, p6) = para
    p1 = angToRad(p1)
    p2 = angToRad(p2)
    p3 = angToRad(p3)
    p4 = angToRad(p4)
    p5 = angToRad(p5)
    p = initPara(p1, p2, p3, p4, p5, p6)
    print('para: ', p)
    p = resultVector(p)
    print('(x, y, z): ', p)
    p = resultFinal(p)
    print('degree: ', radToAng(limitTwoPi(p[0])),' ','direction: ', radToAng(limitTwoPi(p[1])))

# main
def main():
    """
    initDegree: p1
    initPosition: p2
    sensorX: p3
    sensorY: p4
    sensorPosition: p5
    situation: p6
    """
    testFunc = (0.1, 45, 0.2, 0.3, 250, 1)
    func(testFunc)

if __name__ == '__main__':
    main()











