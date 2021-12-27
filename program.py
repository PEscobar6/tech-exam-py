import pandas as pd
datos = pd.read_csv('data.csv', header=0, sep=",")
df_vacio = pd.DataFrame()

datos = datos.sort_values(by='tipo')
percentageA = 0
percentageB = 0
percentageC = 0
percentageD = 0

# Data por cada slice
slice_a = datos.loc[:3]
slice_b = datos.loc[4:7]
slice_c = datos.loc[8:11]
slice_d = datos.loc[12:]

# Totales de cada tipo y nombre
total_a = slice_a.groupby(['tipo'])[['valor']].sum()
total_b = slice_b.groupby(['tipo'])[['valor']].sum()
total_c = slice_c.groupby(['tipo'])[['valor']].sum()
total_d = slice_d.groupby(['tipo'])[['valor']].sum()


def getPercentageOfName(tipo, data, total):
    dictData = {}
    dictData["TIPO"] = tipo
    for item in data.itertuples():
        if(item.nombre == "A"):
            valorItem = round(item.valor)
            dictData["PORCENTAJE_A"] = ((item.valor * 100) / total)
        if(item.nombre == "B"):
            dictData["PORCENTAJE_B"] = (item.valor * 100) / total
        if(item.nombre == "C"):
            dictData["PORCENTAJE_C"] = (item.valor * 100) / total
        if(item.nombre == "D"):
            dictData["PORCENTAJE_D"] = (item.valor * 100) / total
    
    dictData["TOTAL"] = total
    return dictData

responseA = getPercentageOfName(1, slice_a, total_a)
responseB = getPercentageOfName(1, slice_b, total_b)
responseC = getPercentageOfName(1, slice_c, total_c)
responseD = getPercentageOfName(1, slice_d, total_d)

## Agregamos los datos al Dataframe
df_vacio = df_vacio.append(responseA, ignore_index=True)
df_vacio = df_vacio.append(responseB, ignore_index=True)
df_vacio = df_vacio.append(responseC, ignore_index=True)
df_vacio = df_vacio.append(responseD, ignore_index=True)
print(df_vacio.head())