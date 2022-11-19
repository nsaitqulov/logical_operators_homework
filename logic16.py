def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
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

    return x4!=0 and x3*1000+x2*100+x1*10+x!=a
print(main(763))