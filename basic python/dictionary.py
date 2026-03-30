''' 

data = {1:60,2:45, 3:56,'navin':'suraj','goat':'virat'}

print(data.get('goat')) # method 1 
print(data['navin'])  # method 2 
 
-----------------------------------------------------------------

data1 = {1:60,2:45, 3:56,'navin':'suraj','goat':'virat','python':['vscode','jupitarnotr..','online comp..'],'java':{'core':'vscode','spring':'inteli'}}
# dict inside (dict and list) 

-----------------------------------------------------------------

print(data1['python']) # method 1
print(data1['python'][2]) # method 2 list value printing
print(data1['java']['core']) # method 3  dict valaue printing

-----------------------------------------------------------------

data2 = {1:60,2:45, 3:56,'navin':'suraj','goat':'virat'}
print(data2.pop('navin'))
print(data2)
del data2['goat']
print(data2)

-----------------------------------------------------------------

key ={'suraj','rana','king'}  #set
value=[7,77,777] # list   {set and list merging into dict}

dict1 = dict(zip(key,value)) # b y using zip fuction
print(dict1)

'''