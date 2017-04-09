import csv
reader = csv.reader(open("Fl_sample.csv", "r"))
writer = csv.writer(open("copy.csv","w"))
for row in reader:
    writer.writerow(row[1:6])
