#from itertools import product
import db_connector

DEBUG = False

"""
#deprecated due to dictionaries being too strict for this usecase
some_dictionary = {
    "apple": "some page to load, about apples",
    "honey": "some page to load, about honey",
    "water": "some page to load, about water, and rivers",
    "river": "some page to load, about water, and rivers"
}
try:
    user_query = input("What would you like to search?\n")
    for key in some_dictionary:
        if user_query in key:
            print(some_dictionary[key])
except KeyError:
    print("That is not a valid entry")
"""


"""
def fuzzy_search(search_query, fat_finger_dictionary, best_candidate):
    for index, letter in enumerate(search_query):
        #TODO remove after fat_finger_dictionary is completed
        if letter not in fat_finger_dictionary.keys():
            continue
        for replacement in fat_finger_dictionary[letter]:
            #TODO think about too many replacements, most people do not misstype entire paragraphs (tm)
            temp_user_query = search_query[:index] + replacement + search_query[index + 1:]
"""
def build_options(option_query, option_ffd):
    options = []
    for letter in option_query:
        if letter in option_ffd.keys():
            this_set = set(option_ffd[letter])
            this_set.update(letter, "")
            options.append(this_set)
        else:
            this_set = set([letter, ""])
            options.append(this_set)
    return options

def product(*iterables):
    """Cartesian product function"""
    pools = [tuple(it) for it in iterables]
    def walk(depth,prefix):
        if depth == len(pools):
            yield tuple(prefix)
            return
        for item in pools[depth]:
            prefix.append(item)
            yield from walk(depth + 1, prefix)
            prefix.pop()
    yield from walk(0, [])

def get_all_permutations(permutation_query, permutation_ffd):
    all_permutations = []
    for permutation in product(*build_options(permutation_query, permutation_ffd)):
        all_permutations.append(permutation)
    return all_permutations

"""
def basic_recursion():
    return basic_recursion()

#basic_recursion()

def merge_sort(main_list):
    if len(main_list) == 1:
        return main_list
    left_list = merge_sort(main_list[:len(main_list)//2])
    right_list = merge_sort(main_list[len(main_list)//2:])
    merge_list = []
    index_left = 0
    index_right = 0
    while index_left < len(left_list) and index_right < len(right_list):
        if left_list[index_left] < right_list[index_right]:
            merge_list.append(left_list[index_left])
            index_left += 1
        else:
            merge_list.append(right_list[index_right])
            index_right += 1
    if index_left == len(left_list):
        merge_list.extend(right_list[index_right:])
    else:
        merge_list.extend(left_list[index_left:])
    return merge_list

print(merge_sort([2, 5, 7, 3, 6, 0, 10]))
"""

def search_from_query(search_query, internal_search_list, search_best_candidate):
    for index, temp_info in enumerate(internal_search_list):
        info = temp_info[0]
        candidate_score = 1 # 1 is the max value, 0 is a perfect match
        if search_query in info:
            #print(info)
            word_list = info.split(" ")
            for word in word_list:
                if search_query in word:
                    proposed_score = (len(word) - len(search_query)) / len(word) # percent error closeness match
                    """
                    #the next 4 lines are the "rolled out" code of the in-line if immediately after it
                    if proposed_score < candidate_score:
                        candidate_score = proposed_score
                    else:
                        candidate_score = candidate_score
                    """
                    candidate_score = proposed_score if proposed_score < candidate_score else candidate_score
            if search_best_candidate[0] > candidate_score:
                search_best_candidate[0] = candidate_score
                search_best_candidate[1] = index

if __name__ == "__main__":
    fat_finger_dictionary, search_list = db_connector.get_all_from_db()

    user_query = input("What would you like to search?\n")
    best_candidate = [1, None]
    if "y" not in input("Fuzzy search can take a while to complete for long serch queries\nWould you like to perform fuzzy search? y/n\n").lower():
        search_from_query(user_query, search_list, best_candidate) # regular search
    else: # fuzzy search
        for this_permutation in get_all_permutations(user_query, fat_finger_dictionary):
            temp_user_query = "".join(this_permutation)
            if DEBUG:
                print(temp_user_query)
            search_from_query(temp_user_query, search_list, best_candidate)
            """
            for info in search_list:
                candidate_score = 1 # 1 is the max value, 0 is a perfect match
                if temp_user_query in info:
                    #print(info)
                    word_list = info.split(" ")
                    for word in word_list:
                        if temp_user_query in word:
                            proposed_score = (len(word) - len(temp_user_query)) / len(word) # percent error closeness match
                            #the next 4 lines are the "rolled out" code of the in-line if immediately after it
                            #if proposed_score < candidate_score:
                            #    candidate_score = proposed_score
                            #else:
                            #    candidate_score = candidate_score
                            candidate_score = proposed_score if proposed_score < candidate_score else candidate_score
                    if best_candidate[0] > candidate_score:
                        best_candidate[0] = candidate_score
                        best_candidate[1] = info
            """
            #best_candidate has the best matching page here
    print(search_list[best_candidate[1]])