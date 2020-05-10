# ProblemSet 2
# Name : Sun
# Time : 2：00

def evaluate_poly(poly,x):
    ans = float(0)
    length = len(poly)
    for i in range(length):
        ans += float(poly[i] * x ** i)
    return ans

# poly = (0.0, 0.0, 5.0, 9.3, 7.0) 
# x=-13
# res = evaluate_poly(poly,x)
# print ("the ans is : ",res)

# problem 2


def compute_deriv (poly):
    res = []
    if len(poly) < 2:
        return [0.0]
    for j in range(1, len(poly)):
        res.append(float(j * poly[j]))
    return res
# poly = (-13.39, 0.0, 17.5, 3.0, 1.0) 
# print (compute_deriv(poly)) 

def compute_root(poly, x_0, epsilon): 
    root = x_0
    counter = 1
    while abs(evaluate_poly(poly,root))>=epsilon:
        root = (root - evaluate_poly(poly,root)/evaluate_poly(compute_deriv(poly),root))
        # print (root)
        counter += 1
    return [root, counter]

poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
x_0 = 0.1
epsilon = 0.0001
print (compute_root(poly,x_0,epsilon))