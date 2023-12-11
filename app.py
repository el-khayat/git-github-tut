# square.py

def calculate_square(number):
    return number * number

def add(a,b) :
    return a+b ;

def mul(a,b) :
    return a*b ;


if __name__ == "__main__":
    print("Hello world !")
    ns = input("inter a number") 
    
    n =  float(  ns    ) 

    n2 = calculate_square(n)
    print(f"result is {n2}")
    