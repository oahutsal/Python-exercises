'''
Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:

Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с «!», а также строки в которых содержатся слова из списка ignore (ignore = ["duplex", "alias", "Current configuration"]).
Для проверки надо ли игнорировать строку, использовать функцию ignore_command.

Проверить работу функции на примере файла config_sw1.txt
'''
def ignore_command(command, ignore = ["duplex", "alias", "Current configuration", "!"]):
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    command_list = []
    with open(config_filename, 'r') as f:
        for line in f:
            ignore_status = ignore_command(line)
            if ignore_status != True:
                command_list.append(line.strip('\n'))
    keys_list = []
    values_list = []
    vl_list = []
    for i in command_list:
        if i[0] != ' ':
            keys_list.append(i)
            values_list.append(vl_list)
            vl_list = []
        elif i[0] == ' ':
            values_list[-1].append(i)
    config_dict = dict.fromkeys(keys_list)
    n = 0
    while n < len(values_list):
        for key in config_dict:
            config_dict[key] = values_list[n]
            n += 1
    # for key in config_dict:
    #     print(key, ':', config_dict[key])
    for key, value in config_dict.items():
        print(key, ':',value)

convert_config_to_dict('C:/Programming/exercises/09_functions/config_sw1.txt')