def min_value(digits):
    mylist = list(dict.fromkeys(digits))
    mylist.sort()
    my_lst_str = ''.join(map(str, mylist))
    return (int(my_lst_str))
