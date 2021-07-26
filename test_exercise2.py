import random 

def get_random_number():   
    return random.randint(1, 10)

def add_number_with_random_number(a,get_random_number):    
    return a + get_random_number()

#Arrange

expected = 9.2
a=0.2
#aCT
def test_add_number_with_random_number():
    
    def mock_random_number():
        return 9
    
    result = add_number_with_random_number(a,mock_random_number)
    print(result)
    assert result == expected

test_add_number_with_random_number()