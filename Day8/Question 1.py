def fibonacci(function_which_needs_wrap):
    num1 = int(input("Enter number one "))
    num2 = int(input("Enter number two "))

    for no in range(num1,num2):

        sum = 0
        temp = no

        while temp > 0:
            digit = temp % 10
            sum = sum + digit ** 3
            temp = temp // 10

        if no == sum:
            print(no)
            exit
            
        function_which_needs_wrap()
        print("This is wrap function")
   
   
   
   
   
   
@fibonacci
def display():
    print("This is decorator")