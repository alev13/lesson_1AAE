import json
filename = "user_settings2.txt"
myfile =open(filename, mode='w',encoding='Latin-1')

player1= {'playername': "DONALD TRUMP", 'Score': 345, 'awards':["OR","NV","NY"]}
player2= {'playername': "VADIMIR PUTIN", 'Score': 228, 'awards':["MSK","SPB"]}

myplayers=[]
myplayers.append(player1)
myplayers.append(player2)
#==============SAVE by  JSON===========
json.dump(myplayers, myfile)
myfile.close()

