# Code Summary: Lab 1 showing Python environment and basic code file template.

def lab1_averages():
    '''
    Accepts an integer and float value. 
    Calculates and returns the average.
    '''
    myint = int(input("\n\tPlease enter a whole number: "))
    myfloat = float(input("\tPlease enter a decimal number: "))
    return (myint + myfloat)/2

def lab1_concat():
    '''
    Accepts two strings, a first and last name. Concatenates and returns a concatenated string.
    '''
    first = input("\n\tPlease enter your first name: ").lower()
    last = input("\tPlease enter your last name: ").lower()
    return (last.title() + ", " + first.title())

def main():
    '''
    Main driver method that makes function calls to the previous `lab1_concat()` and `lab_1averages()` methods.
    '''
    print("\nWelcome to the first lab.")
    from_concat = lab1_concat()
    from_average = lab1_averages()
    print("\n\t\tResults of Function Calls")
    print("\t\tThe result of running the concat function is {}".format(from_concat))
    print("\t\tThe result of running the average function is {:.2f}".format(from_average))
    print("\nThank you.")
    return

main()
