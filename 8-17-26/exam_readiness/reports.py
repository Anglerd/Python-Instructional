# This file stores functions that print formatted reports

def print_readiness_report(student_name, scores, average_score, readiness_result, weakest_domain, weakest_score):
    print("---------------------")
    print("Exam Readiness Report")
    print("---------------------")
    print("Student", student_name)
    print("Practice Exam Scores:")
    for key in scores:
        print(f"{key}: {scores[key]}")
    print("Average Score:", average_score)
    print("Readiness Result:", readiness_result)
    print("Weakest Domain:", weakest_domain)
    print("Weakest Domain Score:", weakest_score)
    print("---------------------")
