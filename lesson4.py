# shop_cash = [10000, 34000, 30000, 12300, 45000, 90000, 78999]
# expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
# all_cash = sum(shop_cash)
# all_expenses = sum(expenses)
# profit = all_cash - all_expenses
# print(profit)
# shop_cash = [10000, 34000, 30000, 12300, 45000, 90000, 78999]
# expenses = [1000, 3000, 20000, 5000, 5600, 7654, 3425]
# shop_cash2 = [100200, 342000, 300300, 152300, 45000, 90000, 78999]
# expenses2 = [10200, 30020, 200400, 550050, 5600, 7654, 3425]
#
# def get_many(shop_cash : list, expenses : list):
#     all_cash = sum(shop_cash)
#     all_expenses = sum(expenses)
#     profit = all_cash - all_expenses
#     return profit
#
# monday = get_many(shop_cash, expenses)
# day2 = get_many(expenses=expenses2, shop_cash=shop_cash2)
# print(day2)


# *args **kwargs


# def get_argumets(*args, **kwargs):
#     if args:
#         print(args)
#     if kwargs:
#         print(kwargs)
#
# get_argumets()


# d = {
#     'name': 'Nazgul',
#      'age': 26
# }

def get_list_square(*nazgul, **kwargs):
    result = []
    # dicts = {}
    if nazgul:
        for i in nazgul:
            result.append(i**2)
    if kwargs:
        for key, value in kwargs.items():
            if type(value) == str:
                kwargs.update({
                    key: value.upper()
                })
            elif type(value) == set:
                kwargs.update({
                    key: [value]
                })
    return result, kwargs


    # return result
print(get_list_square(1, 3, 7, 11, name="Nazi", age=50, sets={1, 3}))
