import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv('https://kapextmediassl-a.akamaihd.net/IST/IN300/IN300_1905A/Average_Daily_Traffic_Counts.csv', usecols=['Street','Date of Count','Total Passing Vehicle Volume'])
#
# data.columns = [column.replace(" ","_") for column in data.columns]
# data['Date_of_Count'] = pd.to_datetime(data['Date_of_Count'], format='%m/%d/%Y')
# dataQuery1 = data.query('Date_of_Count == "03/02/2006"')
#
# print(dataQuery1)
#
# groupedData = data.groupby('Street')
# result = groupedData.mean(numeric_only=True)
#
# print(result)
#
# result.plot(kind='bar')
# plt.title("Average Vehicle Vol - 3/2/06")
# plt.xlabel("Street")
# plt.ylabel("Average Vehicle Vol")
# plt.xticks(rotation=45, ha='right', fontsize=8)
# plt.legend('', frameon=False)
# plt.tight_layout()
#
# plt.show()

data = pd.read_csv('https://kapextmediassl-a.akamaihd.net/IST/IN300/IN300_1905A/Demographic_Statistics_By_Zip_Code.csv', usecols=['COUNT FEMALE','COUNT MALE'])

data.columns = [column.replace(' ','_') for column in data.columns]
plt.scatter(data['COUNT_FEMALE'], data['COUNT_MALE'], s=50)
plt.title("Scatter Plot - Female/Male Counts")
plt.xlabel("Female Count")
plt.ylabel("Male Count")

plt.show()
