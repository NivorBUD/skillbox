import json

differences_list = ['services', 'staff', 'datetime']
differences_dict = dict()

with open('json_new.json', 'r', encoding='UTF-8') as new_file:
    new_data = json.load(new_file)

with open('json_old.json', 'r', encoding='UTF-8') as old_file:
    old_data = json.load(old_file)


def find_differences(diff_key, old_dict, new_dict):
    for key in new_dict.keys():
        if old_dict[key] != new_dict[key] and key == diff_key:
            return new_dict[key]
        elif key != diff_key and (isinstance(new_dict[key], dict) or isinstance(old_dict[key], dict)):
            value = find_differences(diff_key, old_dict[key], new_dict[key])
            if value:
                return value


for key in differences_list:
    diff = find_differences(key, old_data, new_data)
    if diff:
        differences_dict[key] = diff

print(differences_dict)

with open('result.json', 'w', encoding='UTF-8') as file:
    json.dump(differences_dict, file, indent=4)
