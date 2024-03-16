import numpy as np
r = 2.5
v = 1
vecs = np.array(
    [
 [1.0, 0.0, 2.0],
 [-1.0, 0.5, 2.0],
 [-2.0, 1.5, 0.0],
 [2.5, -1.2, -0.5],
 [1.5, 0.2, -0.2]
    ]
)
print(closest(vecs, v, r)