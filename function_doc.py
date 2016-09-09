def total(initial=0, *numbers, **keywords):
    """
    This function adds all of the numbers given as parameters or keyword
    dictionary entries and returns the total.

    Parameters:
    initial - initial value defaults to 0
    *numbers - any number of numbers separated by commas
    **keywords - any number of name=number pairs e.g. fruit=77

    gp-2015
    """
    count = initial
    for number in numbers:
        count += number #add the numbers stored in a tuple
    for key in keywords:
        count += keywords[key] # add the numbers associated
                               # keywords stored in a dictionary
    return count # Return the result

total_count = total(10, 1, 2, 3, vegetables=50, fruits=100)
print (total_count)
print ('\n')
print (total.__doc__)
help(total)