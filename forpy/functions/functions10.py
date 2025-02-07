def unique_elements(l):
    unique_list=[]

    for item in l:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


print(unique_elements([1, 2, 3, 2, 4, 4, 5]))