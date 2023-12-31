from armstrong_numbers import find_armstrong_numbers

print(find_armstrong_numbers([0])) 
print(find_armstrong_numbers(list(range(0, 8))))
print(find_armstrong_numbers(list(range(0,100))))
print(find_armstrong_numbers(list(range(0,999))))

def test_find_armstrong_numers_0():
    assert find_armstrong_numbers([0]) == 0

def test_find_armstrong_numers_small():
    assert find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7]

def test_find_armstrong_numers_medium():
    assert find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_find_armstrong_numers_large():
    assert find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

