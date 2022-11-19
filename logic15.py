def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
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
    return (x+y+z)%2==1

print(main(335))