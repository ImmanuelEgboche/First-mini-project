import random #Start from the bottom set your assert statements/what you want to test
def get_random_number():
    return random.randint(1, 10)
def add_number_with_random_number(a,get_random_number):   #As this function is dependent on the get random fucntion i replicate this in my mock test
    return a + get_random_number()

# print(add_number_with_random_number(7))
def add_number_with_random_number_test(): #This function is created to call the test to make sure the asserts work
    #Arrange
    a = 2
    expected = 7 
    def mock_get_random_number(): #Create a function within the test function to replicate a example random 
        return 5
    #act 
    result = add_number_with_random_number(a,mock_get_random_number) #This test makes sure the addition is correct however a extra arguement is passed in
    
    assert result == expected # get_random_number is passed in as it is dependant to the add_number_with_random_number function
    
add_number_with_random_number_test() 