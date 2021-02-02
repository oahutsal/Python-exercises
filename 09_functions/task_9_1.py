'''
Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает такие аргументы:

1. Cловарь с соответствием интерфейс-VLAN такого вида:

{"FastEthernet0/12": 10,
 "FastEthernet0/14": 11,
 "FastEthernet0/16": 17}

2. Шаблон конфигурации access-портов в виде списка команд (список access_mode_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template. В конце строк в списке не должно быть символа перевода строки.
'''

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

def generate_access_config(intf_vlan_mapping, access_template):
    config_list = []
    for i in intf_vlan_mapping:
        config_list.append(f'\ninterface {i}')
        for command in access_template:
            if command == 'switchport access vlan':
                config_list.append(f'switchport access vlan {intf_vlan_mapping[i]}')
            else:
                config_list.append(command)
    return config_list
a = generate_access_config(access_config, access_mode_template)
for item in a:
    print(item)