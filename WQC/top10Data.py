import pandas as pd

# data_file = 'data.xlsx'
# df = pd.read_excel(data_file)

# Count the number of times a station is used
# print(df['Start Station Id'].value_counts().to_string())

# print(df['End Station Id'].value_counts().to_string())
# sums = df.groupby(['Start Station Id', 'End Station Id']).size().reset_index(name='Count')
# sort the values by the count
# sums = sums.sort_values(by='Count', ascending=False)
# f = open("demofile2.txt", "a")
# f.write(sums.to_string())
# f.close()


# put the top 10 station ids in a list
# station_ids = df['Start Station Id'].value_counts().head(10).index.tolist()

station_ids = [7033, 7417, 7030, 7378, 7581, 7640, 7357, 7006, 7378, 7543]

# write an excel file for the data only from the top 10 station ids
# df[df['Start Station Id'].isin(station_ids)].to_excel('q2stations.xlsx')

q2_file = 'q2stations.xlsx'
q2 = pd.read_excel(q2_file)





# regex to output only the time from the following: 01/01/2024 00:50
# print(df['Start Time'].str.extract(r'(\d{2}:\d{2})').to_string())