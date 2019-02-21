

# Algorithm based on https://stackoverflow.com/questions/9004789
# Uses Gauss-Legendre algorithm
# https://en.wikipedia.org/wiki/Gauss–Legendre_algorithm
def pi(n):
    if n <= 0:
        return None
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    digits = []
    while len(digits) < n:
        if 4 * q + r - t < m * t:
            digits.append(str(m))
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2
    if len(digits) > 1:
        digits = digits[:1] + ['.'] + digits[1:]
    return "".join(digits)
