def function(a = 1, b = 2, c = 3):
    return int(a + b / c)
x = function(2, c = 1, b = 2)
print(x)