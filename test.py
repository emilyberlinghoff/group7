import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
# Replace 'your_data.csv' with the path to your actual data file
df = pd.read_excel('WQC hackathon ride-sharing data.xlsx')

# Convert 'Start Time' and 'End Time' to datetime format
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['End Time'] = pd.to_datetime(df['End Time'])

# Identify major intersections by counting the occurrences of start and end stations
major_intersections_start = df['Start Station'].value_counts().head(10)
major_intersections_end = df['End Station'].value_counts().head(10)

# Analyze peak times
df['Start Hour'] = df['Start Time'].dt.hour
peak_times = df['Start Hour'].value_counts().sort_index()

# Frequent paths
frequent_paths = df.groupby(['Start Station', 'End Station']).size().reset_index(name='Counts')
frequent_paths = frequent_paths.sort_values(by='Counts', ascending=False).head(10)

# Visualization
# Major Intersections
plt.figure(figsize=(10, 6))
sns.barplot(x=major_intersections_start.values, y=major_intersections_start.index)
plt.title('Top 10 Major Start Intersections')
plt.xlabel('Number of Trips Started')
plt.ylabel('Start Station')
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x=major_intersections_end.values, y=major_intersections_end.index)
plt.title('Top 10 Major End Intersections')
plt.xlabel('Number of Trips Ended')
plt.ylabel('End Station')
plt.show()

# Peak Times
plt.figure(figsize=(10, 6))
sns.lineplot(x=peak_times.index, y=peak_times.values)
plt.title('Bike Usage by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Trips')
plt.xticks(range(0, 24))
plt.grid(True)
plt.show()

# For frequent paths, consider creating a visualization that makes sense for your analysis,
# like a network graph, if you have the tools, or simply list the top paths.

print(frequent_paths)
