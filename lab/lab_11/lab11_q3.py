def count_vowels(filename):
    try:
        file_obj = open(filename, 'r')
    except FileNotFoundError:
        return {}

    dict = {}

    a_count = 0
    e_count = 0
    i_count = 0
    o_count = 0
    u_count = 0
    for line in file_obj:
        line = line.strip().upper()  # 全都先变成大写，这样在罗列 if 条件时就能少列一条

        for i in line:
            a_count += 1 if i == "A" else 0 # 如果等于 A 就 + 1，不然就加 0 
            e_count += 1 if i == "E" else 0
            i_count += 1 if i == "I" else 0
            o_count += 1 if i == "O" else 0
            u_count += 1 if i == "U" else 0
    
    file_obj.close()

    dict["A"] = a_count 
    dict["E"] = e_count 
    dict["I"] = i_count 
    dict["O"] = o_count 
    dict["U"] = u_count

    tup = tuple(dict.items()) # 先把dict 变成一个tuple of tuples， 然后看哪个key对应的value 是 0，则删除那个key
    for i in range(len(tup)):
        if tup[i][1] == 0:
            key = tup[i][0]
            del dict[key]
        
    return dict

def main():
    dict = count_vowels("lab\lab_11\count_vowls.txt")
    print(dict)
main()