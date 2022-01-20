# def list_method():
#     pass
#
#
# # for(int index)
#
# list_variable = [1, 2, 3, 4, 5, 6, 7]
# print(type(list_variable))
#
# for first_index in range(len(list_variable)):
#     print(first_index)
#
# print(list_variable[1])


def loop_over_username(**kwargs):
    username = (input("Enter name: "))
    username1 = (input("Enter name: "))
    username2 = (input("Enter name: "))
    username3 = (input("Enter name: "))
    username4 = (input("Enter name: "))
    username_list = [username, username1, username2, username4, username3]
    for name in username_list:
        print(name)


print(loop_over_username())
