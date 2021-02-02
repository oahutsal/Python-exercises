'''
Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта выглядит так:

interface FastEthernet0/20
 switchport mode access
 duplex auto
 
То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
'''
def get_int_vlan_map(config_filename):
    config_sw1 = []
    #Витяг всіх строк які починаються з interface або switchport з файлу
    with open(config_filename, 'r') as f:
        for line in f:
            if line.startswith('interface') or line.lstrip().startswith('switchport'):
                config_sw1.append(line.strip())
    access_list = []
    trunk_list = []
    eth_list = []
    #Поділ на trunk або access
    for i in config_sw1:
        if i.startswith('interface'):
            if 'switchport mode access' in eth_list:
                access_list.append(eth_list)
                eth_list = []
            elif 'switchport mode trunk' in eth_list:
                trunk_list.append(eth_list)
                eth_list = []
            eth_list.append(i)
        else:
            eth_list.append(i)
    access_keys = []
    access_keys_VL1 = []
    access_vlans = []
    #Поділ на ключ:значеня access
    for i in access_list:
        if len(i) == 2:
            for itm in i:
                if itm.startswith('interface'):
                    access_keys_VL1.append(itm.split()[-1])
        if len(i) == 3:
            for itm in i:
                if itm.startswith('interface'):
                    access_keys.append(itm.split()[-1])
                elif itm.startswith('switchport access'):
                    access_vlans.append(itm.split()[-1])
    trunk_keys = []
    trunk_vlans = []
    #Поділ на ключ:значеня trunk
    for i in trunk_list:
        for itm in i:
            if itm.startswith('interface'):
                trunk_keys.append(itm.split()[-1])
            elif itm.startswith('switchport trunk allowed vlan'):
                trunk_vlans.append(itm.split()[-1])
    #Cловник з портами VLAN 1
    access_dict_VL1 = dict.fromkeys(access_keys_VL1, 'port in VLAN 1')
    #Словник з портами в режимі access
    access_dict = dict.fromkeys(access_keys)
    #Присвоєння значення vlan до FastEthernet в режимі access({'FastEthernet0/0': '10', 'FastEthernet0/2': '20', 'FastEthernet1/0': '20', 'FastEthernet1/1': '30', 'FastEthernet1/3': 'port in VLAN 1', 'FastEthernet2/0': 'port in VLAN 1', 'FastEthernet2/1': 'port in VLAN 1'})
    ac = 0
    while ac < len(access_vlans):
        for i in access_dict:
            access_dict[i] = access_vlans[ac]
            ac += 1
    #Словник з портами в режимі trunk
    trunk_dict = dict.fromkeys(trunk_keys)
    #Присвоєння значення vlan(у вигляді списку) до FastEthernet в режимі trunk ({'FastEthernet0/1': ['100', '200'], 'FastEthernet0/3': ['100', '300', '400', '500', '600'], 'FastEthernet1/2': ['400', '500', '600']})
    tr = 0
    while tr < len(trunk_vlans):
        for i in trunk_dict:
            trunk_dict[i] = trunk_vlans[tr].split(',')
            tr += 1
    #З'єднання двох словників
    access_dict.update(access_dict_VL1)
    #Кортеж з двох словників
    tuple_dicts = (access_dict, trunk_dict)
    return tuple_dicts
a = get_int_vlan_map('C:/Programming/exercises/09_functions/config_sw2.txt')
print(a)