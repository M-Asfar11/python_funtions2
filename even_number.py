def get_even_number():
    try:
        num = int(input("Enter number"))
        if(num % 2  == 0):
            print("number is even")
        else: 
            print("number is odd")
    except ValueError:
        print("plese enter integer value")
        
get_even_number()