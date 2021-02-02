'''
Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:

ключи: имена интерфейсов, вида «FastEthernet0/1»
значения: список команд, который надо выполнить на этом интерфейсе
Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.
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
    keys = []
    command_list = []
    for i in intf_vlan_mapping:
        c_list = []
        keys.append(i)
        for command in trunk_template:
            if command == 'switchport trunk allowed vlan':
                list_to_str = ','.join(map(str, intf_vlan_mapping[i]))
                c_list.append('{} {}'.format(command, list_to_str))
            else:
                c_list.append(command)
        command_list.append(c_list)
    config_dict = dict.fromkeys(keys)
    #print(config_dict)
    #print(command_list)
    i = 0
    while i < len(command_list): 
        for val in config_dict:
            config_dict[val] = command_list[i]
            i += 1
    return config_dict
a = generate_trunk_config(trunk_config, trunk_mode_template)
print(a)