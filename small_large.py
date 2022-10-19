

def digits(n):
    largest = 0
    smallest = 9
 
    while (n):
        r = n % 10
 
        # Find the largest digit
        largest = max(r, largest)
 
        # Find the smallest digit
        smallest = min(r, smallest)
 
        n = n // 10
 
    print(largest,smallest)
 
 

 
n = int(input("Enter the testing integer : "))
 

digits(n)
 