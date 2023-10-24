import random

print("Задание 1")

def get_line_length(line, line_num):
    length = len(i_line)
    try:
        if i_line.endswith("\n"):
            length -= 1
        if length < 3:
            raise BaseException
    except BaseException:
        print("Ошибка: менее трёх символов в строке {}".format(line_num))
    return length


summ = 0
line_num = 0
try:
    with open("people.txt", "r", encoding="UTF-8") as people:
        for i_line in people:
            line_num += 1
            summ += get_line_length(i_line, line_num)
finally:
    print("Общее количество символов:", summ)

print("\nЗадание 2")
summ = 0
try:
    with open("out_file.txt", "w") as data:
        while summ < 777:
            num = int(input("Введите число: "))
            data.write(str(num) + "\n")
            unlucky_num = random.randint(1, 14)
            if unlucky_num == 13:
                raise BaseException
            summ += num
except BaseException:
    print("Вас постигла неудача")
else:
    print("Вы успешно выполнили условие для выхода из порочного цикла!")

print("\nЗадание 3")

def validate_line(line):
    try:
        if len(line.split()) < 3:
            raise IndexError
        name, email, age = line.split()
        if not name.isalpha():
            raise NameError
        if not (email.count('.') != 0 and email.count('@') != 0):
            raise SyntaxError
        if not (10 <= int(age) <= 100):
            raise ValueError
    except IndexError:
        bad.write(line + "    " + "НЕ присутствуют все три поля\n")
    except NameError:
        bad.write(line + "    " + "Поле «Имя» содержит НЕ только буквы\n")
    except SyntaxError:
        bad.write(line + "    " + "Поле «Имейл» НЕ содержит @ и точку\n")
    except ValueError:
        bad.write(line + "    " + "Поле «Возраст» НЕ представляет число от 10 до 99\n")
    else:
        good.write(line + "\n")


data = open('registrations.txt', 'r', encoding='UTF-8')
bad = open('registrations_bad.log', 'w', encoding='UTF-8')
good = open('registrations_good.log', 'w', encoding='UTF-8')
for i_data in data:
    validate_line(i_data[:-1])


print("\nЗадание 4")
chat = open("chat.txt", "a", encoding="UTF-8")
def write_message(name):
    message = input("Введите сообщение: ")
    chat.write("{}: {}\n".format(name, message))


def print_chat():
    chat = open("chat.txt", "r", encoding="UTF-8")
    for i_message in chat:
        print(i_message[:-1])
    chat.close()


name = input("Введите имя пользователя: ")
answer = int(input("Выберите действие: \n"
                   "1. Посмотреть текущий текст чата\n"
                   "2. Отправить сообщение \n"))
if answer == 1:
    print_chat()
elif answer == 2:
    write_message(name)

chat.close()


print("\nЗадание 5")
def get_square(num):
    try:
        num = int(num)
        if num < 0:
            raise SyntaxError
        return num ** 0.5
    except SyntaxError:
        print("Это отрицательное число!")

    except ValueError:
        print("Это не число!")


print("asd")
print(get_square("asd"))

print(-3)
print(get_square(-3))

print(5)
print(5, get_square(5))