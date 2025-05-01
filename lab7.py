A = [1, 3, 5, 10, 12, 8, 15, 7, 20, 3, 9, 4]

with open("original_data.txt", "w") as f:
    f.write(" ".join(map(str, A)))

with open("original_data.txt", "r") as f:
    data = list(map(int, f.read().split()))

greater_than_9 = [num for num in data if num > 9]

sum_gt_9 = sum(greater_than_9)

with open("greater_than_9.txt", "w") as f:
    f.write(" ".join(map(str, greater_than_9)))

print(f"9-dan böyük ədədlər: {greater_than_9}")
print(f"9-dan böyük ədədlərin cəmi: {sum_gt_9}")
