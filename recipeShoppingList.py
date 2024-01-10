import pandas as pd 
import numpy as np 


ingredientTypes2 = {}
shoppingList = {}
recipes = ['recipe 1','recipe 2']

for rec in recipes:
    recipe = pd.read_excel('shoppingTest.xlsx',sheet_name=rec)
    ingredientTypes = {
    'dairy':[],
    'produce':[],
    'seasonings':[],
    'grains':[],
    'protein':[],
    'misc':[]
    }
    for col in recipe.columns:
        try:
            ing = col.split()[0]
            ingredientTypes[ing].append(list(recipe[col]))
            ingredientTypes2[ing] = np.array(ingredientTypes[ing]).T
        except:
            pass
    total = []
    for i in ingredientTypes2:
        for u in ingredientTypes2[i]:
            u = list(u)
            total.append(u)
    print(total)
    print()


    for i in ingredientTypes2:
        for u in ingredientTypes2[i]:
            u = list(u)
            while 'nan' in u:
                u.remove('nan')
            combine = ' '.join(u)
            if i not in shoppingList:
                shoppingList[i] = [combine]
            else:
                shoppingList[i].append(combine)
    lens = []
    for i in shoppingList:
        shoppingList[i].sort(reverse=1)
        lens.append(len(shoppingList[i]))
# print(shoppingList)

while len(set(lens)) > 1:
    smallest = min(lens)
    smallestIndx = lens.index(smallest)
    keys = list(shoppingList.keys())
    shoppingList[keys[smallestIndx]].append(None)
    lens = []
    for i in shoppingList:
        lens.append(len(shoppingList[i]))



# print(shoppingList)
dF = pd.DataFrame(shoppingList)
count = 1
x = ''
for i in range(len(shoppingList)-1):
    dF.insert(i+count,x,None)
    count += 1
    x += ' '
dF.to_csv('test.csv',index=0)
