def is_even(number):
    if number % 2 == 0:
        return True
    return False


def list_of_positives(lst):
    res_list = []
    for n in lst:
        if n > 0:
            res_list.append(n)

    return res_list


def compare_nr_of(no1, no2):

    if no1 > no2:
        return no1
    elif no2 > no1:
        return no2
    else:
        return None
