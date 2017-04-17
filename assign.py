def first_derivative(x, y):
    return (3 * x * y) # 3xy

def second_derivative(x, y, d1 = None):
    d1 = first_derivative(x, y) if (d1 is None) else d1

    return ((d1 * 3 * x) + (3 * y)) # 3x *(dy/dx) + 3y

def third_derivative(x, y, d1=None, d2=None):
    d1 = first_derivative(x, y) if (d1 is None) else d1
    d2 = second_derivative(x, y, d1) if (d2 is None) else d2

    # 3x *d/dx(dy/dx) + 6(dy/dx)
    return (3 * x * d2) + (6 * (d1))

h = 0.1

def f(x,y):
    d1 = first_derivative(x, y)
    d2 = second_derivative(x, y, d1)
    d3 = third_derivative(x, y, d1, d2)
    return y + (
        h * d1
    ) + (
        ((h * h )/(2 * 1)) * d2
    ) + (
        ((h * h * h) / (3 * 2 * 1))* d3
    )

X = [(x * h) for x in range(1,11)]

results = [('0.0', 0.5)]

for i, x in enumerate(X):
    x_p = x - h
    y_p = results[i][1]
    result = f(x_p, y_p)
    results.append(("{:.1f}".format(x), result))

('0.0', 0.5)
('0.1', 0.5075)
('0.2', 0.5307965337499999)
('0.3', 0.5720585330975899)
('0.4', 0.6352833002633351)
('0.5', 0.7269470570917312)
('0.6', 0.8571160145022194)
('0.7', 1.0412862467703403)
('0.8', 1.3034232910341694)
('0.9', 1.6810302321399326)
('1.0', 2.2337201923780157)
