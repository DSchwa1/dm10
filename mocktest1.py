from operator import truediv


def get_consultant_name():
    first_name = 'Dylan'
    surname = 'Schwartz'
    email = 'dylanschwartz@kubrickgroup.com'
    return first_name, surname, email

print(get_consultant_name())

# EVERY SECOND EQUAL
def every_second_equal(x,y):
    if len(x) == len(y) and x[1::3] == y[1::3]:
        return True
    else:
        return False
print('EVERY SECOND EQUAL TEST')
print(f'EXPECTED: True --- ACTUAL: {every_second_equal([99,1,123,3], [0,1,2,3])}')
print(f'EXPECTED: False --- ACTUAL: {every_second_equal([1,123,3,99], [1,321,3,101])}')

# Odd Numbers
def odd_numbers1(x):  
    temp = list()
    for i in x:
        if i is True:
            temp.append(i)
        if (type(i) == int or type(i) == float) and i%2 == 1: 
            temp.append(i)
    return temp

print('ODD NUMBERS TEST')
print(f"EXPECTED: [1,3,3] --- ACTUAL: {odd_numbers1([1,2,3,3,'3'])}")
print(f'EXPECTED: [True,3, 5.0] --- ACTUAL: {odd_numbers1([False,True,3,5.0,7.5])}')

#NAME PROCESSING 1
def name_processing1(list_of_names):
    m = list()
    for i in list_of_names:
        x = i.split(' ')
        if len(x) == 1:
            x.append(None)
        m.append(x)
    return m


print('NAME PROCESSING 1 TEST')
print("EXPECTED: [['Diego', 'Maradona'], ['Ronaldo', None], ['Cormac', 'McArthy'], ['Eminem', None]]") 
print(f"ACTUAL: { name_processing1(['Diego Maradona', 'Ronaldo', 'Cormac McCarthy', 'Eminem'])}")

#NAME PROCESSING 2
def name_processing2(list_of_names2):
    m = list()
    for i in list_of_names2:
        k = dict()
        x = i.split(' ')
        if len(x) == 1:
            k['mononym'] = x[0]
        else:
            k['first_name'] = x[0]
            k['second_name'] = x[1]

        m.append(k)
    return m

print('NAME PROCESSING 2 TEST')
print("EXPECTED: [{'first_name': 'Diego', 'second_name': 'Maradona'},{'mononym': 'Ronaldo'},{first_name': 'Cormac', 'second_name': 'McCarthy'}, {'mononym': 'Eminem'}]") 
print(f"ACTUAL: {name_processing2(['Diego Maradona', 'Ronaldo', 'Cormac McCarthy', 'Eminem'])}")

#NOISE GENERATOR
import random

def noise_generator(noise_prob):  
   x=random.randint(-1,1)
   p = int
   if x == 0:
       p = 1 - noise_prob
   else:
        p = noise_prob/2
   yield f'{x} : {p}::'
    
    

print('NOISE GENERATOR TEST')
print(f'ACTUAL: {next(noise_generator(.6))} {next(noise_generator(.6))} {next(noise_generator(.6))}')

