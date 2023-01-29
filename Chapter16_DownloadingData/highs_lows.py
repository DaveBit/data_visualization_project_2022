import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:  # we open the file and store the file object in F
    reader = csv.reader(f)  # Creating a reader object associated with the F file. Storing it in Reader.
    header_row = next(reader)  # We use the next() function from the csv module.
    print(header_row)

