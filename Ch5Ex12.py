Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def max(integer1, integer2):
	if integer1 > integer2:
		return integer1
	else:
		return integer2

	
>>> print( "Let's determine which of two integers is greater." )
Let's determine which of two integers is greater.
>>> num1 = int(input( "Enter the first integer: "))
Enter the first integer: 5
>>> num2 = int(input( "Enter the second integer: "))
Enter the second integer: 8
>>> print("\nThe greater value is", str(max(num1, num2)) + '.')

The greater value is 8.
>>> 
