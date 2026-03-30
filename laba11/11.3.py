import math

def trig_expression(x, n):
    if n == 1:
        return math.sin(x) * math.cos(x)
    elif n == 2:
        return math.sin(x ** 2) + math.cos(x)
    else:
        return 1 - math.sin(x)
 
x_val = math.pi / 4  
 
for n_val in [1, 2, 3]:
    result = trig_expression(x_val, n_val)
    if n_val == 1:
        formula = "sin(x)*cos(x)"
    elif n_val == 2:
        formula = "sin(x²)+cos(x)"
    else:
        formula = "1-sin(x)"
    print(f"n={n_val}: {formula} при x=п/4: {result:.6f}")