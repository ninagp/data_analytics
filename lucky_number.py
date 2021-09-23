"""Derive all numbers from a string and check if the numbers are lucky.
If a number is equal to the sum of its digits ^ 3, then the number is Lucky, if not, the number is Unlucky.
Numbers cannot be more than 3 digits in length."""
def is_sum_of_cubes(s):
    t = "".join([' ', el][el.isdigit()] for el in s)
    numbers = t.split(" ")  #turn a list into a string

    clean_list = []  # clean the list off spaces
    for el in numbers:
        if el != '':
            clean_list.append(el)

    for el in clean_list:
        if len(el) > 3:  # if length of an element is more than 3 symbols, the element gets divided into a three-symbol part and a "tale". The tale and the three symbols get added to the list until the tale length is less than or equals to three symbols.
            clean_list.append(el[0:3])
            clean_list.append(el[3:len(el)])


    for el in clean_list:
        if len(el) > 3:
            clean_list.remove(el)  # Cleaning the list off all the elements that exceed three symbols in length.

    print(clean_list)
    for el in clean_list:
        # Calculating the sum of digits ^ 3 of numbers in the list
        sum_num = sum(int(x) ** 3 for x in el)
        print(['Unlucky', 'Lucky'][int(el) == sum_num]) #if a number is equal to the sum of each of its digits ^ 3, the number is Lucky, if not - Unlucky.


is_sum_of_cubes("&z _upon 40729899999a --- ???ry, ww/100 I thought, 6311str*ng and w===y -721&()153")