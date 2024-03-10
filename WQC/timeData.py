import pandas as pd
# The error indicates there is no 'Start Station' column in the dataframe. 
# Let's inspect the dataframe to understand its structure and correct the column names.

# Load the data from the provided Excel file
file_path = 'q2stations.xlsx'
df = pd.read_excel(file_path)

# The column we're interested in is 'Start Station Name'. Let's proceed with the analysis using the correct column name.

# Convert 'Start Time' to datetime
df['End Time'] = pd.to_datetime(df['End Time'])

# Define the time intervals as hour bins
time_bins = [i for i in range(25)]  # 0, 1, 2, ..., 24

# Label for the intervals
time_labels = [
    "00:00-01:00", "01:00-02:00", "02:00-03:00", "03:00-04:00",
    "04:00-05:00", "05:00-06:00", "06:00-07:00", "07:00-08:00",
    "08:00-09:00", "09:00-10:00", "10:00-11:00", "11:00-12:00",
    "12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00",
    "16:00-17:00", "17:00-18:00", "18:00-19:00", "19:00-20:00",
    "20:00-21:00", "21:00-22:00", "22:00-23:00", "23:00-00:00"
]

# Assign each start time to an interval
df['Time Interval'] = pd.cut(df['End Time'].dt.hour, bins=time_bins, labels=time_labels, right=False)

# Now we count the number of rides started from each station during each time interval
# Group by 'Start Station Name' and 'Time Interval' and count occurrences
ride_counts = df.groupby(['Start Station Name', 'Time Interval']).size().unstack(fill_value=0)

# Save the results to a new Excel file
output_file = 'end_ride_counts.xlsx'
ride_counts.to_excel(output_file)