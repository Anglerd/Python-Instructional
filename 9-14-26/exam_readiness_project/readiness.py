# Week 3 Day 1 Readiness Logic
# This file stores functions used to determine exam readiness


def calculate_average(some_list: list):
    """
    Calculates the average of a given list of numbers
    params=some_list of only numbers
    output=float average
    """
    """
    index = 0
    this_sum = 0
    while index < len(some_list):
        this_sum += some_list[index]
        index += 1
    this_sum /= index
    """
    return_value = 0
    for index, number in enumerate(some_list):
        return_value += number
    return_value /= len(some_list)
    return return_value


def determine_readiness(average_score):
    """
    :param average_score:
    :return: average_score >= 85? "Exam Ready"
    average_score >= 70 and <85?? "Needs More Practice"
    average_score < 70? "Not Ready"
    """
    # statement if condition_true else: statement_false
    # statement1 if condition1_true else: statement2 if condition2_true else: statement_false
    if average_score >= 85:
        return "Exam Ready"
    elif average_score >= 70:
        return "Needs More Practice"
    else:
        return "Not Ready"
    # return "Exam Ready" if average_score >= 85 else "Needs More Practice" if average_score >= 70 else "Not Ready"


"""
def smallest_number(some_list: list):
    some_list = sorted(some_list)
    return some_list[0]

    smallest_value is first value in list
    then for each value in the rest of the list,
        check if the new value is smaller than smallest_value
        if the new value is smaller than smallest_value
            smallest_value is not the new value
    after checking all values in the list, smallest_value is the smallest_value in the list

    smallest_value = some_list[0]
    for value in some_list:
        if value < smallest_value:
            smallest_value = value
    return smallest_value
"""


def identify_weak_area(domain_scores: dict):
    """
    weakest_domain is the first key in the dictionary
    smallest_number is the value associated with weakest_domain in the dictionary
    then for each key in the dictionary
        if the associated value with that key is lower than smallest_number
            then weakest_domain is the new key
            and smallest_number is the value associated with that key
    after checking all keys in the dictionary, weakest_domain is the name of the key with the lowest value
    and smallest_number is the score of that domain
    """
    weakest_domain = None
    for key in domain_scores:
        if not weakest_domain or domain_scores[key] < smallest_number:
            weakest_domain = key
            smallest_number = domain_scores[key]
    return weakest_domain, smallest_number


if __name__ == "__main__":
    test_list = [4, 5, 6]
    # print(calculate_average(test_list))
    print(determine_readiness(86))
    test_scores = {
        "key1": 1,
        "key2": 2
    }
    print(identify_weak_area(test_scores))