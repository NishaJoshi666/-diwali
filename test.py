import pandas as pd

df = pd.read_csv("CleanedData.csv")
print(df.head())

df.drop(["Unnamed: 0"], axis = 1 , inplace = True)
df["Radius"] = df["Radius"].apply(lambda x:x.replace("$","").replace(",","")).astype("float")

Radius =df["Radius"].to_list()
Mass = df["Mass"].to_list()

gravity = []

def SI(Radius,Mass):
    for i in range(0,len(Radius)-1):
        Radius[i] = Radius[i]* 6.957e+8
        Mass[i] = Mass[i]* 1.989e+30

SI(Radius,Mass)

def FindGravity(Radius,Mass):
    G = 6.674e-11
    for i in range(0,len(Mass)):
        g = (G*Mass[i])/(Radius[i]*Radius[i])
        gravity.append(g)

FindGravity(Radius,Mass)

df["Gravity"] = gravity

print(df.head())

df.to_csv('stars_with_gravity.csv')
