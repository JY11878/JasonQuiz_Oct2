#The first step is define the function
def main():
#Then get the input from users
    celsius= float(input("Please tell me the Celsius Degrees:"))
#write the equation of converting celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32
#output the result
    print("The temperature in fahrenheit is", fahrenheit)
#call the function
main()
