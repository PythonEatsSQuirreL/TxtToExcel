import csv

txt_file = r"test.txt"
csv_file = r"test.csv"

in_txt = csv.reader(open(txt_file, "r"), delimiter = "\t")
out_csv = csv.writer(open(csv_file, 'w'))

out_csv.writerows(in_txt)

del out_csv
