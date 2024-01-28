import copy
# None ko chay, 0 chạy hết
#==================================Bản gốc==================================
Account = []
boss_JoinRally = {
    'port': 0,
    'ip': "127.0.0.1",
    'do':0,
    'champ':2,
    'meat':5,
    'ymir': None,
    'pumkin': None,
    'sphinx': None,
    'witch': None,
    'hydra': None,
    'golem': None,
    'turtle': None,
    'warlord': None,
    'nor': None,
    'cerberus': None
}

buttonTabChange = []
#============================================================================

#=========================Copy mới cho mỗi tab===============================
def addNew():
    Account.append(copy.deepcopy(boss_JoinRally))
    
def addButtonTab(tab):
    buttonTabChange.append(tab)

    

    