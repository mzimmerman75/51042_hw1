# Problem 3


def f(x):
    return(x - 1) ** 2

def f_pr(x):
    return(2 * (x - 1))

def f2(x):
    return (x**2)-4

def f2_pr(x):
    return 2*x


def newton(f, f_pr, x_0, tol, max_iter):

    #this function takes in parameters of multiple other functions defined above
    #the parameters are single variable equations and derivatives of those equations
    #the parameters are also pre defined from the problem such as tol and max_iter
    #the return value is the newton-raphson method with aditional specification depending on the values of x_0, tol, and max_iter

    recurrences = 1
    
    while recurrences <= max_iter:
        if f_pr(x_0) == 0:
            break
        
        x_n = (x_0 - (f(x_0) / f_pr(x_0)))

        x_0 = x_n

        recurrences += 1


    return(x_0)



#print(newton(f, f_pr, 0, 1e-16, 1))
#print(newton(f2, f2_pr, 1, 1e-16, 1000))
#print(newton(f, f_pr, 0, 1e-16, 1000000))