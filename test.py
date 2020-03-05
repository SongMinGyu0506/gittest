num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")

print("this is test1 branch")

'''input_d = int(input())
student_list = []

for i in range(student_list):
    weight, height = map(int, input().split())
    student_list.append(weight,height)

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank = rank+1
        print(rank, end=' ')'''
