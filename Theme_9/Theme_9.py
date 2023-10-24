import os
import zipfile

print("Задание 1")
def calc_2():
    numbers_file = open("numbers.txt", "r")
    answer = open("answer.txt", "w")
    nums_sum = 0
    for i_line in numbers_file:
        nums_sum += i_line.count("2") * 2
    numbers_file.close()
    answer.write(str(nums_sum))

calc_2()

print("\nЗадание 2")
def reverse_print_file(file_name):
    zen = open(file_name, 'r')
    zen_data = zen.read().split('\n')
    for i in range(len(zen_data) - 1, -1, -1):
        print(zen_data[i])

reverse_print_file("zen.txt")


print("\nЗадание 3")
def calc_files_size(path_to_folder, res_size, files_count, dirs_count):
    elems = os.listdir(path_to_folder)
    for i_elem in os.listdir(path_to_folder):
        way = os.path.abspath(os.path.join(path_to_folder, i_elem))
        if os.path.isdir(way):

            res_size, files_count, dirs_count = calc_files_size(way, res_size, files_count, dirs_count + 1)
        else:
            res_size += os.path.getsize(way) / 1024
            files_count += 1
    return res_size, files_count, dirs_count


size, files, dirs = calc_files_size(os.path.abspath(os.path.join("../..", "..", "Skillbox")), 0, 0, 0)
print("Размер каталога (в Кбайтах):", size)
print("Количество подкаталогов:", dirs)
print("Количество файлов:", files)

print("\nЗадание 4")

def get_second_tour_players():
    first_tour = open("first_tour.txt", "r")
    second_tour_players = {}
    points = 0
    for i_line in first_tour:
        line = i_line.split()
        if len(line) <= 2:
            points = int(i_line.split()[0])
            continue
        player = line[1][:1] + ". " + line[0]
        player_points = int(line[2])
        if player_points > points:
            second_tour_players[player] = player_points
    return points, sorted(second_tour_players.items(), key=lambda x: -x[1])

def write_results_to_file():
    second_tour = open("second_tour.txt", "w")
    points, second_tour_players = get_second_tour_players()
    second_tour.write(str(points) + "\n")
    for i in range(len(second_tour_players)):
        second_tour.write("{0}) {name} {points}\n".format(i + 1,
                                                          name=second_tour_players[i][0],
                                                          points=second_tour_players[i][1]))

write_results_to_file()

print("\nЗадание 5")
def make_frequency_dict(text_file):
    frequency_dict = {}
    text_letters_count = 0
    for line in text_file:
        for letter in line.lower():
            if letter in "qwertyuiopasdfghjklzxcvbnm":
                text_letters_count += 1
                if letter in frequency_dict:
                    frequency_dict[letter] += 1
                else:
                    frequency_dict[letter] = 1
    return frequency_dict, text_letters_count


def make_rev_frequency_dict(frequency_dict, text_letters_count):
    rev_frequency_dict = {}
    for letter in frequency_dict.keys():
        k = round(frequency_dict[letter] / text_letters_count, 3)
        if k in rev_frequency_dict:
            rev_frequency_dict[k] += letter
        else:
            rev_frequency_dict[k] = letter
    return sorted(rev_frequency_dict.items(), key=lambda x: -x[0])


text = open("text.txt", "r")
frequency_dict, text_letters_count = make_frequency_dict(text)
rev_frequency_dict = make_rev_frequency_dict(frequency_dict, text_letters_count)
analysis = open("analysis.txt", "w")
for k, letters in rev_frequency_dict:
    letters = sorted(letters)
    for i_letter in letters:
        analysis.write(" ".join([i_letter, str(k), '\n']))


print("\nЗадание 6")
zip_file = zipfile.ZipFile("voina-i-mir.zip", "r")
text = zip_file.read("voina-i-mir.txt").decode("UTF-8")
zip_file.close()

letters = sorted([(let, text.count(let)) for let in text if let.isalpha()], key=lambda x: -x[1])
answer = open("answer_6.txt", "w", encoding="UTF-8")
for letter, count in letters:
    answer.write(letter + ":" + str(count) + "\n")
answer.close()
