import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']

for i in range(len(phone_numbers)):
    phone_pattern = r"\b[89][1234567890]{9}\b"
    res = re.search(phone_pattern, phone_numbers[i])
    if res:
        print('{} номер: всё в порядке'.format(i + 1))
    else:
        print('{} номер: не подходит'.format(i + 1))
