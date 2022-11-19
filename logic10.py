def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a//10
    a//=10
    y=a%10
    return x!=0 and x+y!=a

print(main(4))