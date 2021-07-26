def add_two_numbers(a,b):
    return a+b

# Arrange

expected = "sas4"
#Act 

def add_two_numbers_test(a,b):
    try:
        if a or b == type(str):
            x = str(a)+ str(b)
            return x
        else:
            return a+b
    except:
        AssertionError
        print("invalid input")

result = add_two_numbers_test(True,"4")
# print(result)
#Assert - Passed
# assert result == expected