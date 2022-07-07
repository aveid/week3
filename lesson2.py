# set1 = {
#     1, 2, 3, 4, 5
# }
# set2 = {1, 2, 3, 4, 5, 4, 6}
# set1 = {"Hello", "banana"}
# set2 = {"Hello", "banana"}
# set3 = {"Hello", "potato", "orange"}
# print(set1.intersection(set3, set2))
# set1.update(set2)
# # print(set1.union(set2))
# print(set1.isdisjoint(set2))
# if set2.issuperset(set1) and set1.issuperset(set2):
#     print("Это супермножество")
# # elif set1 == set2:
# #     print("они равны")
# else:
#     print("Это no супермножество")
#
# if set1 == set2:
#     print("они равны")


# comprehentions - lists, dict

# lists = []
# for i in range(1, 10001):
#     lists.append(i)
# print(lists)
# str1 = "skjdnkd;'dgbv'pekrverkbv;erl'v'er"
# lists = [i for i in str1]
# print(lists)

# import datetime


# print(time_now)

# lists = []
# time_now = datetime.datetime.now()
# for i in range(1, 10001):
#     lists.append(i)
# delta = datetime.datetime.now() - time_now
# print(delta)

# time_now = datetime.datetime.now()
# lists = [i for i in range(1, 10001)]
# delta = datetime.datetime.now() - time_now
# print(delta)

# lists = [i**2 for i in range(1, 10001) if i % 2 == 0 and i % 5 == 0]
# print(lists)

# 3! = 6

# number = int(input())
# fact = 1
# for i in range(1, number + 1):
#     fact *= i
#     print(fact)
# j = 1
# lists = [i for i in range(1, number +1)]

# dicts = {i: i**2 for i in range(1, 5)}
# print(dicts)
# lists = ['apple', 'banana']
# dicts = {i: i*3 for i in lists}
# print(dicts)

def test_func():
    print("Hello world")