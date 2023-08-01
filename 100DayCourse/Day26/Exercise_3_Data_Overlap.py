with open("100DayCourse/Day26/file1.txt") as file1:
    file1_nums = file1.readlines()

with open("100DayCourse/Day26/file2.txt") as file2:
    file2_nums = file2.readlines()

result = [int(num) for num in file1_nums if num in file2_nums]

print(result)

    