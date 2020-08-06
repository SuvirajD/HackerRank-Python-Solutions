if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    for marks in student_marks[query_name]:
        total += marks
    print('{:.2f}'.format(total/3))
