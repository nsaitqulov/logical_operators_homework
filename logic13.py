def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a%10
    a//=10
    y=a%10
    return (x+y)%2==0
print(main(35))