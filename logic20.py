def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    x=n%10
    n//=10

    x1=n%10
    n//=10

    x2=n%10
    n//=10

    x3=n%10
    n//=10

    x4=n%10

    if x+x1+x2+x3+x4>2:
        return "True"
    if x+x1+x2+x3+x4<=2:
        return "False"
print(main(1100))