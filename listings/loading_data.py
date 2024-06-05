network_data1 = pd.read_csv('02-15-2018.csv', low_memory=False)
network_data2 = pd.read_csv('02-16-2018.csv', low_memory=False)
network_data3 = pd.read_csv('02-20-2018.csv', low_memory=False)
network_data4 = pd.read_csv('02-21-2018.csv', low_memory=False)

network_data3.drop(columns=['Flow ID', 'Src IP', 'Src Port', 'Dst IP'], axis=1,inplace=True)

network_data = pd.concat([network_data1, network_data2], axis=0)
network_data.reset_index(drop=True, inplace=True)
del network_data1, network_data2

network_data = pd.concat([network_data, network_data3], axis=0)
network_data.reset_index(drop=True, inplace=True)
del network_data3

network_data = pd.concat([network_data, network_data4], axis=0)
network_data.reset_index(drop=True, inplace=True)
del network_data4