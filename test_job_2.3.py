import math
import numpy as np

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)) * 180/math.pi 

p11 = 17.0047876456793361
p12 = 99.8322813181069506
p21 = 17.0048320892817024
p22 = 99.8325186262986790
p31 = 17.0047693036156592
p32 = 99.8327459622259568
v1 = (p21-p11,p22-p12)
v2 = (p21-p31,p22-p32)
print(angle_between(v1, v2))  # หามุมของจุด p2 ที่อยู่ระหว่าง p1,p3

