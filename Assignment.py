def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8, 1]

final_list = remove_duplicates(my_list)

print(final_list)