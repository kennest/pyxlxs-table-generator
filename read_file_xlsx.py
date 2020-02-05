import pandas as pd
from sql import create_table,alter_table
#on ouvre le fichier excel
file_name = '/home/davis/Documents/CRF_CVS_VF/DDD_Lascope_2.xlsx' 
df = pd.read_excel(file_name, sheet_name='TABLE')
print(df.head())
#show_table()
#create_table('TEST_PY')
tables=[]
fields=[]
sizes=[]
types=[]
descriptions=[]
references=[]
parameters=[]

for i,item in enumerate(df['TABLE']):
    tables.append(str(item))
print(len(tables))

for i,item in enumerate(df['DESCRIPTION']):
    descriptions.append(str(item))
print(len(descriptions))

for i,item in enumerate(df['REFERENCE']):
    references.append(str(item))
print(len(descriptions))

for y,field in enumerate(df['CODE']):
    fields.append(str(field))
print(len(fields))

for y,size in enumerate(df['TAILLE']):
    sizes.append(str(size))
print(len(sizes))

for y,tpe in enumerate(df['TYPE']):
    types.append(str(tpe))
print(len(types))

table_set=set(tables)

for i in range(len(tables)):
        #si le début du nom du champ est composé des 3 dernière lettres du nom de la table
        #alors on l'ajoute aux paramètres
        #if fields[i].startswith(str(tables[i])[-3:]):
        line=[]
        if descriptions[i]=='Clé étrangère':
            line=(str(tables[i]),str(fields[i]),str(sizes[i]),str(types[i]),2,str(references[i]))
        elif descriptions[i]=='Clé primaire':
            line=(str(tables[i]),str(fields[i]),str(sizes[i]),str(types[i]),1,str(references[i]))
        else:
            line=(str(tables[i]),str(fields[i]),str(sizes[i]),str(types[i]),0,str(references[i]))
            
        parameters.append(line)
            #print("field data =>",str(tables[i])+'/'+str(fields[i]))
print(parameters)    
print(len(table_set))
for t in table_set:
    create_table(t)

for p in parameters:
    alter_table(p)
