def get_degree(list_):
    print list_
    dict_ = {}
    count = 1
    for i in list_:
        if i not in dict_:
            dict_[i] = count
        else:
            dict_[i] = dict_[i] + 1
    return max(dict_.items(), key=lambda x: x[1])[1]


if __name__ == "__main__":
    x = int(raw_input())
    l = raw_input().split(' ')
    print(get_degree(l))
