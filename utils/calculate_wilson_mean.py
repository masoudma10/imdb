from math import sqrt

def confidence(like, dislike):
    """
    wilson mean algorithm
    :param like:
    :param dislike:
    :return:  average rate
    """

    n = like + dislike

    if n == 0:
        return 0

    z = 1.0
    phat = float(like) / n
    return ((phat + z*z/(2*n) - z * sqrt((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n))