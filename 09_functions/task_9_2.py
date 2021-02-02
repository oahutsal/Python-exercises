'''
Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

У функции должны быть такие параметры:

1. intf_vlan_mapping: ожидает как аргумент словарь с соответствием интерфейс-VLANы такого вида:

{"FastEthernet0/1": [10, 20],
 "FastEthernet0/2": [11, 30],
 "FastEthernet0/4": [17]}

2. trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)
Функция должна возвращать список команд с конфигурацией на основе указанных портов и шаблона trunk_mode_template. В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря trunk_config и списка команд trunk_mode_template. Если эта проверка прошла успешно, проверить работу функции еще раз на словаре trunk_config_2 и убедится, что в итоговом списке правильные номера интерфейсов и вланов.
'''

trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(intf_vlan_mapping, trunk_template):
    config_list = []
    for i in intf_vlan_mapping:
        config_list.append(f'interface {i}')
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                list_to_str = ','.join(map(str, intf_vlan_mapping[i]))
                config_list.append('{} {}'.format(command, list_to_str))
            else:
                config_list.append(command)
    return config_list
a = generate_trunk_config(trunk_config, trunk_mode_template)
for i in a:
    print(i)