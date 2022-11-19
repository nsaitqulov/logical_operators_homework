def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    a//=10
    y=a%10
    a//=10
    z=a%10
    return z!=0 and x*10+y!=a
print(main(9))