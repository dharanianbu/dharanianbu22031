# your code goes here
# taking input from user
number = int(input("Enter any number: "))
 
# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number,"not prime")
            break
    else:
        print(number,"prime")
 
# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number,"not prime")
