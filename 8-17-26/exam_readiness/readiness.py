# This file stores reusable functions for exam readiness calculations

DEBUG = False
"""
def mergersort(list):
    length = len(list)
    if len(list) > 1:
        left = mergersort(list[:length/2])
        right = mergersort((list[length/2:]))
    else:
        return list
    index_left = 0
    index_right = 0
    index = 0
    merge = []
    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            merge[index] = left[index_left]
            index_left += 1
        else:
            merge[index] = right[index_right]
            index_right += 1
        index += 1
    if index_left == len(left):
        for num in right[index_right:]:
            merge[index] = num
            index += 1
    else:
        for num in left[index_left:]:
            merge[index] = num
            index += 1
    return merge
"""


def calc_avg(num_1, num_2):
    return (num_1 + num_2) / 2


def calculate_averages(num_list: list):
    if not num_list:
        print("ERROR:nothing in num_list while calculating several averages in readiness")
        return None
    if len(num_list) <= 1:
        print("ERROR:not many values in num_list while calculating many averages")
    return sum(num_list) / len(num_list)


def identify_weak_area(domain_scores: dict):
    weakest_domain = min(domain_scores, key=domain_scores.get)
    weakest_score = domain_scores[weakest_domain]
    return weakest_domain, weakest_score


def determine_readiness(average_score):
    if average_score >= 85:
        return "Exam Ready"
    elif average_score >= 70:
        return "Needs More Practice"
    else:
        return "Not Ready"
