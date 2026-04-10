#task1
# def even_numbers(n):
#     for i in range(1, n + 1):
#         yield i * 2
#
# for num in even_numbers(5):
#     print(num)








#task2
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# fib = fibonacci()
# for i in range(10):
#     print(next(fib))
#
# x= 5
# the_list = 1 if x % 2 == 0 else 0






#task3
# students = [("Ibroxim", 98), ("Shohrux", 90), ("Shoabdurahmon", 85)]
#
# sorted_students = sorted(students, key=lambda x: x[1])
#
# print(sorted_students)














#task4
# nums = [10, 55, 23, 89, 42, 70]
#
# result = list(filter(lambda x: x > 50, nums))
#
# print(result)












#task5
def read_errors(filename):
    with open(filename, "r") as file:
        for line in file:
            if "ERROR" in line:
                print(line.strip())

read_errors("log.txt")










#task6
# def warning_lines(filename):
#     with open(filename, "r") as file:
#         for line in file:
#             if "WARNING" in line:
#                 yield line.strip()
#
# for line in warning_lines("log.txt"):
#     print(line)
















#task7
# def read_file(filename):
#     with open(filename, "r") as f:
#         for line in f:
#             yield line.strip()
#
# def filter_errors(lines):
#     for line in lines:
#         if "ERROR" in line:
#             yield line
#
# def to_upper(lines):
#     for line in lines:
#         yield line.upper()
#
# lines = read_file("log.txt")
# errors = filter_errors(lines)
# result = to_upper(errors)
#
# for line in result:
#     print(line)
















#task8
# def process(filename):
#     with open(filename) as f:
#         for line in f:
#             if "ERROR" in line:
#                 yield line.upper()
#
# for line in process("log.txt"):
#     print(line)









#task9
# import time, random
#
# def event_stream():
#     events = ["EVENT1", "EVENT2", "EVENT3"]
#     while True:
#         yield random.choice(events)
#         time.sleep(1)
#
# stream = event_stream()
# for i in range(5):
#     print(next(stream))










#task10
# from pathlib import Path
# def read_csv_filtered(filename):
#     path = Path(filename)
#
#     try:
#         with path.open("r", encoding="utf-8") as f:
#             next(f)
#             for line in f:
#                 parts = line.strip().split(",")
#
#                 if len(parts) != 2:
#                     continue
#
#                 name, age = parts
#
#                 if age.isdigit() and int(age) > 30:
#                     yield name, int(age)
#
#     except FileNotFoundError:
#         print(f"Error: file '{filename}' not found")

#
# def read_csv_filtered(filename):
#     with open(filename, "r") as f:
#         next(f)
#         for line in f:
#             name, age = line.strip().split(",")
#             if int(age) > 30:
#                 yield name, int(age)
#
# for row in read_csv_filtered("data.csv"):
#     print(row)