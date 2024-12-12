import random

def pair_of_numbers (num):
    list_pair_of_numbers = []
    for i in range (1, num):
        for j in range(1, 20):
            if num % (i + j) == 0 and i <= j and i != j:
                list_pair_of_numbers.append(i)
                list_pair_of_numbers.append(j)
    return list_pair_of_numbers

random_number = random.randint (3, 20)
print (random_number, '\n', *pair_of_numbers(random_number))
