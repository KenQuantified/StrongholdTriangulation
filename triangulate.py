import math

def triangulatesh(x1, z1, h1, x2, z2, h2):
    m1 = math.sin(math.radians(-1*h1))/math.cos(math.radians(-1*h1))
    m2 = math.sin(math.radians(-1*h2))/math.cos(math.radians(-1*h2))
    b1 = x1-m1*z1
    b2 = x2-m2*z2
    z3 = (b2 - b1)/(m1 - m2)
    x3 = m1*z3+b1
    return x3, z3
    
def start():
    x1 = -1534     #x-position of first throw
    z1 = 958     #z-position of first throw
    h1 = -43.3    #heading of first throw
    x2 = -1580     #x-position of second throw
    z2 = 1022     #z-position of second throw
    h2 = -93.3     #heading of second throw
    shx, shz = triangulatesh(x1, z1, h1, x2, z2, h2)
    print("Stronghold_x:", shx)
    print("Stronghold_z:", shz)
    
start()