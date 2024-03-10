import pandas as pd

# Load the dataset (replace with the correct path to your file)
excel_path = 'path_to_your_excel_file.xlsx'
df = pd.read_excel(excel_path)

# Ensure column names match your dataset's structure
# For example, if your timestamp column is named "Start Time", replace 'Timestamp' with 'Start Time'
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Create an 'Hour' column based on the 'Timestamp'
df['Hour'] = df['Timestamp'].dt.hour

# Define downtown stations (replace with actual station IDs from your dataset)
downtown_stations = ['Station1', 'Station2']

# Filter for rides in downtown stations
downtown_rides = df[df['Station ID'].isin(downtown_stations)]

# Assuming 'Action' indicates whether a ride is a check-in or check-out
check_ins = downtown_rides[downtown_rides['Action'] == 'Check-in'].groupby('Hour').size()
check_outs = downtown_rides[downtown_rides['Action'] == 'Check-out'].groupby('Hour').size()

# Calculate net flow of bikes for each hour (check-outs - check-ins)
net_flow = check_outs - check_ins

# Print the net flow of bikes for each hour in the downtown area
print(net_flow)
