#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    #create an empty list to store result
    result = []

    #iterate through list1 and list2 and quotient to result
    try:
        for i in range(list_length):
            quotient = my_list_1[i] = my_list_2[i]
            result.append(quotient)
    except TypeError:
        result.append(0)
        print("wrong type")
    except ZeroDivisionError:
        result.append(0)
        print("division by 0")
    except IndexError:
        result.append(0)
        print("out of range")
    finally:
        return result
