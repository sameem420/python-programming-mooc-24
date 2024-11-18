# Write your solution here
students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size? "))
print(f"Number of groups formed: {(students + desired_group_size - 1) // desired_group_size}")
