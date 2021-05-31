print("Hello Welcome in Caluculator")
print("Select Any Operations")
print("1. For Add = 1")
print("2. For Substract = 2")
print("3. For Multiply = 3")
print("4. For Divide = 4")

while True:
    choice = input("Enter Your Choice ( 1 / 2 / 3 / 4)")
    
    if choice in ('1','2','3','4'):
        a = float(input("Enter Your First Value:-"))
        b = float(input("Enter Your Second Value:-"))
        
        if choice == '1': 
            c = a + b
            print("The Answer is :- ", c)
            
        elif choice == '2': 
            c = a - b
            print("The Answer is :- ", c)
        elif choice == '3': 
            c = a * b
            print("The Answer is :- ", c)
        elif choice == '4': 
            c = a / b
            print("The Answer is :- ", c)    
    
    else:
        print("INPUT IS INVALID!")
    
    