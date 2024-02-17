def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
                   if n % i == 0:
                      return False
    return True

number= int(input("Enter the Number"))

if isprime(number):
    print("its prime")
else:
    print("its not prime")
    
                  
                   
