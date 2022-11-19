def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    a//=10
    x1=a%10
    a//=10
    x2=a%10
    a//=10
    x3=a%10
    a//=10
    x4=a%10
    return x4<x3 and x3<x2 and x2<x1 and x1<x

print(main(12347))