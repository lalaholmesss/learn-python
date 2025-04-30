class MathUtilities:
    @staticmethod
    def AddTwoNumbersAndSquareThem(a, b):
        return (a + b) ** 2


# From mathfile import MathUtilities 
# We can import the MathUtilities to access the AddTwoNumbersAndSquareThem method / function

print(MathUtilities.AddTwoNumbersAndSquareThem(2, 3))