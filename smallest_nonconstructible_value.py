def smallest_nonconstructible_value(list_):
    if list_ is []:
        return 0
    max_constructible_value = 0
    for num in list_:
        if num > max_constructible_value + 1:
            break
        else:
            max_constructible_value += num
    return max_constructible_value + 1


if __name__ == "__main__":
    print smallest_nonconstructible_value([1,2,2,4,12,15])
