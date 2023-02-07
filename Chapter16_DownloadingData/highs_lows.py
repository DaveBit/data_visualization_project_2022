import csv
from matplotlib import pyplot as plt
from datetime import datetime


#  First part consist of getting the file and extracting the data.

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:  # we open the file and store the file object in F
    reader = csv.reader(f)  # Creating a reader object associated with the F file. Storing it in Reader.
    header_row = next(reader)  # We use the next() function from the csv module.
    # And we retrieve the first line. Returns a list.

    dates, highs = [], []
    for row in reader:  # The reader stood in the second line, the first one was already read in line 6.
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)  # row[1] returns the max temperature parameter of each row.


# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))  # it is always a good practice to create a fig to add subplotes
# or cover other needs.
plt.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
"""
for index, column_header in enumerate(header_row):  # enumerate() gives you the index and the value.
    print(index, column_header)"""
