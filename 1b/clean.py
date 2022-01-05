import pandas as pd


stations = {
188 : 'AURN Bristol Centre',
203 : 'Brislington Depot',
206 : 'Rupert Street',
209 : 'IKEA M32',
213 : 'Old Market',
215 : 'Parson Street School',
228 : 'Temple Meads Station',
270 : 'Wells Road',
271 : 'Trailer Portway P&R',
375 : 'Newfoundland Road Police Station',
395 : "Shiner's Garage",
452 : 'AURN St Pauls',
447 : 'Bath Road',
459 : 'Cheltenham Road \ Station Road',
463 : 'Fishponds Road',
481 : 'CREATE Centre Roof',
500 : 'Temple Way',
501 : 'Colston Avenue'
}
data = pd.read_csv("bristol-air-quality-data.csv", sep=';', low_memory=False)
df = pd.DataFrame(data)




df.dropna(subset=["SiteID"], inplace=True)



index=0
for row in list(zip(df["SiteID"], df["Location"])):
    if int(row[0]) in stations:
        if stations[int(row[0])] != row[1]:
            df.drop(index, inplace=True)
    else:
        df.drop(index, inplace=True)
    index+=1

df.to_csv("clean.csv", index=False)