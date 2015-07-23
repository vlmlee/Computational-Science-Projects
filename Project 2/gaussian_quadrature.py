"""
Adapted from Mark Newman's code from the book "Computational Physics with Python"

PHYS440: Computational Physics
Project 2, Differentiation, Integration, and Root Finding

"""

from numpy import ones, copy, cos, tan, pi, linspace, abs

def f(x):
    return x**4

def gaussxw(N):
    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))
    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)
    return x,w

if __name__ == "__main__":

    N = 5
    a = 0.0
    b = 2.0

    # Calculate the sample points and weights, then map them
    # to the required integration domain
    x, w = gaussxw(N)
    xp = 0.5*(b-a)*x + 0.5*(b+a)
    wp = 0.5*(b-a)*w

    # Perform the integration
    s = 0.0
    for k in range(N):
        s += wp[k]*f(xp[k])

    error = abs(s - 2**5 / 5.)
    print "The value for the Gaussian Quadrature rule is %f and its error value is %e" \
                                                                    % (s, error)