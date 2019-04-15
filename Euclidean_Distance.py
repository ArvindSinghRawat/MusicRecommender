def euc_dis( ls1, ls2 ):
    """
        Requires two lists of same size where size depicts the number of dimensions
        Returns Euclidean Distance of two points represented by ls1 and ls2
    """
    a = len(ls1)
    sum = 0.0
    for i in range(a):
        diff = ls2[i] - ls1[i]
        diff = diff ** 2
        sum += diff
    sum = sum ** 0.5
    return sum