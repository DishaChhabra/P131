import csv
import pandas as pd

rows = []
with open("data.csv" , "r") as f:
    a = csv.reader(f)
    for i in a:
        rows.append(i)

planet_data_rows = rows[1:]
temp_planet_data_rows = list(planet_data_rows)

radii = []
masses = []
for i in range(0,len(temp_planet_data_rows)):
    radii.append(temp_planet_data_rows[i][4])
    masses.append(temp_planet_data_rows[i][3])

gravity=[]
for i in range(0, len(radii)):
    gravityy = (float(masses[i])* 1.989e+30) / (float(radii[i])*float(radii[i])*6.957e+8*6.957e+8) * 6.673e-11
    gravity.append(gravityy)
    planet_data_rows[i].append(gravityy)

print(len(gravity))

df = pd.read_csv("data.csv")
df['Gravity'] = gravity
print(df)
df.to_csv('data131.csv')















