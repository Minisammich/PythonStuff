def is_prime(N):
    """
    Determines whether a given positive integer is prime or not
    input: N, any positive integer.
    returns: True if N is prime, False otherwise.
    """
    # special cases:
    if N == 1:
        return False

    # the biggest divisor we're going to try
    divisor = N // 2
    while divisor > 1:
        if N % divisor == 0:
            # we found a number that is a factor of N            
            return False
        divisor = divisor - 1
        
    return True
    

    