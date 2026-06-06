import pandas as pd

data=pd.read_csv("titanic.txt")
print(data.head())
print(data.info())
print(data.describe())
print(data.isnull().sum())

print(data["Age"].mean())
print(data["Fare"].max())

# data["Percent"]=(data["Sex"]/data["Survived"])*100
# print(data["Percent"].mean())
print(data.groupby("Sex")["Survived"].mean())
print(data.groupby("Pclass")["Survived"].mean())
meta=data.groupby("Pclass")["Age"].mean()
print(meta)

print(meta.max())
print(meta.min())
for i ,f in meta.items():
    print(f"The mean for {i} class is: {f}")
metaa=data.groupby("Pclass")["Age"].max()
for i ,f in metaa.items():
    print(f"The max for {i} class is: {f}")
metaaa=data.groupby("Pclass")["Age"].min()
smallest=metaaa.min()
for i ,f in metaaa.items():
    print(f"The min for {i} class is: {f}")
if smallest:
    print(smallest)

price_diff=data.groupby("Sex")["Fare"].mean()
print(price_diff)
for i,f in price_diff.items():
    print(f"The average fare for {i}  is: {f}")

smallest=price_diff.min()
print(f"the smallest fare is: {smallest}")

print(data[["Pclass","Survived","Sex"]])
print()
print(data["Sex"].size)
print(data["Survived"].sum())
