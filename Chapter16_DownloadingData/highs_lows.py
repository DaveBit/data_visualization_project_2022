import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:  # we open the file and store the file object in F
    reader = csv.reader(f)  # Creating a reader object associated with the F file. Storing it in Reader.
    header_row = next(reader)  # We use the next() function from the csv module.
    # And we retrieve the first line. Returns a list.
    highs = []

    for row in reader:  # The reader stood in the second line, the first 1 was already read in line 6.
        high = int(row[1])
        highs.append(high)  # row[1] returns the max temperature parameter of each row.

    print(highs)

"""
for index, column_header in enumerate(header_row):  # enumerate() gives you the index and the value.
    print(index, column_header)"""
