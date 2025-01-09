num = int(input("Enter a number: "))
if num == 2:
    print("this number is prime")
if num>2:
    for i in range(2,num):
        if num%i == 0:
            print("this number is not prime")
            break
            
    else:
        print("this number is prime")
            
            