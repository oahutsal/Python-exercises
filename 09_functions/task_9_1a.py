'''
Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли настроен port-security:

имя параметра «psecurity»
по умолчанию значение None
для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)
Функция должна возвращать список всех портов в режиме access с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан. В конце строк в списке не должно быть символа перевода строки.

Проверить работу функции на примере словаря access_config, с генерацией конфигурации port-security и без.
'''

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    config_list = []
    for i in intf_vlan_mapping:
        config_list.append(f'\ninterface {i}')
        for command in access_template:
            if command == 'switchport access vlan':
                config_list.append(f'switchport access vlan {intf_vlan_mapping[i]}')
            else:
                config_list.append(command)
        if type(psecurity) == list:
            for templ in psecurity:
                config_list.append(templ)
    return config_list
a = generate_access_config(access_config, access_mode_template, port_security_template)
for i in a:
    print(i)
# print(a)