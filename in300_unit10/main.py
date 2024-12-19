import pandas as pd

data = pd.read_csv("https://kapextmediassl-a.akamaihd.net/IST/IN300/IN300_1905A/IN300_Dataset1.csv", sep=',', decimal='.', header=0)

print(data.groupby(["Source", "Destination", "Protocol", "Length", "Info"]).size().nlargest(1))