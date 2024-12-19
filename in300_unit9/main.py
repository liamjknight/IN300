import pandas as pd


def printResults(message,value):
    print("\n\n")
    print(message)
    print()
    print(value)


data = pd.read_csv("https://kapextmediassl-a.akamaihd.net/IST/IN300/IN300_1905A/IN300_Dataset1.csv", sep=',',
                   decimal='.', header=0)
printResults("Source IP", data['Source'].value_counts())
printResults("Destination IP", data['Destination'].value_counts())
printResults("Protocol", data['Protocol'].value_counts())

