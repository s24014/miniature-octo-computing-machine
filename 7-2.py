def list_del_nth(list_, index):
    try:
        del list[index]
    except IndexError:
        print('Index Not Found')
    except:
        print('Unexpected Error')
    else:
        print('succesfully')

my_list = ['a', 'b', 'c', 'd']
list_del_nth(my_list, '5')
list_del_nth(my_list, 5)
list_del_nth(my_list, 0)

print(my_list)


