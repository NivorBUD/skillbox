# print("Задание 1")
# def print_nums(num, end):
#     if num == end + 1:
#         return
#     print(num)
#     print_nums(num + 1, end)
#
#
# print_nums(1, int(input("Введите num: ")))

# print("\nЗадание 2")
# site = {
#     'html': {
#         'head': {
#             'title': 'Мой сайт'
#         },
#         'body': {
#             'h2': 'Здесь будет мой заголовок',
#             'div': 'Тут, наверное, какой-то блок',
#             'p': 'А вот здесь новый абзац'
#         }
#     }
# }
#
#
# def find_key(struct, key, max_depth=-1, depth=1):
#     if key in struct:
#         return struct[key]
#     elif depth == max_depth:
#         return None
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = find_key(sub_struct, key, max_depth, depth + 1)
#             if result:
#                 break
#     else:
#         result = None
#
#     return result
#
#
# user_key = input("Введите искомый ключ: ")
# depth_answer = input("Хотите ввести максимальную глубину? Y/N: ")
# if depth_answer in ["y", "Y"]:
#     max_depth = int(input("Введите максимальную глубину: "))
#     print(find_key(site, user_key, max_depth))
# else:
#     print(find_key(site, user_key))

# print("\nЗадание 3")
# def save_new_site(sites_dict, company):
#     sites_dict[company] = "\n".join(["{",
#                                      "\t'html': {",
#                                      "\t\t'head': {",
#                                      "\t\t\t'title': 'Куплю/продам {} недорого'".format(company),
#                                      "\t\t},",
#                                      "\t\t'body': {",
#                                      "\t\t\t'h2': 'У нас самая низкая цена на {}',".format(company),
#                                      "\t\t\t'div': 'Купить',",
#                                      "\t\t\t'p': 'Продать'",
#                                      "\t\t}",
#                                      "\t}",
#                                      "}"])
#
#
# def print_sites(sites_dict):
#     print(len(sites_dict))
#     for i_company, i_site in sites_dict.items():
#         print("Сайт для", i_company)
#         print(i_site)
#         print()
#
#
# sites_dict = {}
# sites_count = int(input("Сколько сайтов: "))
# for i in range(sites_count):
#     company = input("Введите название продукта для нового сайта: ")
#     save_new_site(sites_dict, company)
#     print_sites(sites_dict)

# print("\nЗадание 4")
# def pro_sum(*args):
#     result = 0
#     for i_element in args:
#         if isinstance(i_element, list):
#             for i_num in i_element:
#                 result += pro_sum(i_num)
#         else:
#             result += i_element
#     return result
#
#
# print(pro_sum([[1, 2, [3]], [1]], [[[3, [5], [5]]]]))

# print("\nЗадание 5")
# def open_lists(arr):
#     result = []
#     for i_element in arr:
#         if isinstance(i_element, list):
#             result += open_lists(i_element)
#         else:
#             result += [i_element]
#     return result
#
#
# nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
# print(open_lists(nice_list))

print("\nЗадание 6")
def hoar_sort(my_nums_list):
    less, same, bigger = get_lists(my_nums_list)
    if len(less) != 0:
        less = hoar_sort(less)
    if len(bigger) != 0:
        bigger = hoar_sort(bigger)
    return less + same + bigger


def get_lists(nums_list):
    less = []
    same = []
    bigger = []
    last_number = nums_list[len(nums_list) - 1]
    for num in nums_list:
        if num < last_number:
            less.append(num)
        elif num == last_number:
            same.append(num)
        else:
            bigger.append(num)
    return less, same, bigger


nums_list = [5, 8, 9, 4, 2, 9, 1, 8]
print(hoar_sort(nums_list))
