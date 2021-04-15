sorted_list_1 = [1, 5, 9, 12, 75, 89, 111, 256]
list_of_words = "hi hello cat dog parrot otter milk mink"
sorted_list_2 = sorted(list_of_words.split())
lil_list = [0, 1, 2]


def find_index(list, value):
    left = 0
    right = len(list) - 1
    # mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == value:
            return mid
        elif list[mid] > value:
            right = mid - 1
        elif list[mid] < value:
            left = mid + 1
    return 1


print(find_index(sorted_list_1, 75))
print(find_index(sorted_list_2, "bat"))



