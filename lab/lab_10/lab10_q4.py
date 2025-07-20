import random

def shuffle_create(lst):
    new_lst = []
    length = len(lst)
    for i in range(length):
        random_num = random.randrange(0,len(lst))
        new_lst.append(lst[random_num])
        lst.remove(lst[random_num])
        print(lst)
    
    return new_lst

def shuffle_in_place(lst):
    for i in range(len(lst)-1): # 最后一个数不用换，因为在到最后一个数之前，一定都已经和其他数换过位置了
        j = random.randrange(i+1,len(lst))
        lst[i], lst[j] = lst[j], lst[i]
    return lst

def main():
    list_one = ["Jean Valjean", "Javert", "Fantine", "Cosette", "Marius Pontmercy", "Eponine", "Enjolras"]
    print("ORIGINAL LIST_ONE: {}".format(list_one))
    # First function execution
    print("LIST CREATED BY SHUFFLE_CREATE: {}\n".format(shuffle_create(list_one)))
    
    list_two = ["A", 0, 0, 5, 1, 3, 2]
    print("ORIGINAL LIST_TWO: {}".format(list_two))
    # Second function execution
    shuffle_in_place(list_two)
    print("LIST_TWO AFTER SHUFFLE_IN_PLACE: {}".format(list_two))
main()
