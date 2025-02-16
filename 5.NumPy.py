# Check how many dimensions the arrays have
import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(a.ndim) # NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as jo
g=jo.array(56)
l=jo.array([5,6,4,2,3,5])
o=jo.array([[2,3,4],[4,5,6]])
p=jo.array([[[1,2,3],[4,5,6]],[[2,3,45],[452,5456,3654]],[[1,12,241],[14,3,132]]])
print(g.ndim)
print(l.ndim)
print(o.ndim)
print(p.ndim)

