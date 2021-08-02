from random import randint
def get_random_number():    
    return randint(1, 10)
def add_two_random_numbers(get_random_number):    
    return get_random_number() + get_random_number()

expected = 18
def add_two_random_numbers_test():
    #Arrange
    #Act
    def mock_get_random_number():
        return 9
    result = add_two_random_numbers(mock_get_random_number) 
    print(result)
    assert expected == result 

add_two_random_numbers_test()