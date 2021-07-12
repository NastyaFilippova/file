import os
print(os.getcwd())
os.chdir(r'C:\Users\aphilippova\PycharmProjects\file\text')

file_list = ['1.txt', '2.txt', '3.txt']
for file in file_list:
    with open(file, 'r', encoding='utf-8') as read_file:
        name = file
        lines = read_file.readlines()
        len_lines = len(lines)


    with open('write.txt', 'a', encoding='utf-8') as write_list:
        write_list.write(f'{name}\n')
        write_list.write(f'{len_lines}\n')
        write_list.writelines(lines)
        write_list.write('\n')
