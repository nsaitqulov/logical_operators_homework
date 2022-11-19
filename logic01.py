def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    x=a<b
    x1=b<c
    x3=x and x1
    y=a>b
    y1=b>c
    y3=y and y1
    return x3 or y3

print(main(6, 5, 4))