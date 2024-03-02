import numpy as np
a = [1, 2, 3, 4, 5, 6]
b = [10, 11, 12, 13, 14, 15]
x = np.min((np.max(a), np.min(b)))
print(x)
