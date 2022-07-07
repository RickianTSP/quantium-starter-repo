import csv

with open('Filtered_Data.csv', mode='w') as csv_file_w:
    fieldnames = ['Sales', 'Date', 'Region']
    writer = csv.DictWriter(csv_file_w, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(3):
        with open("daily_sales_data_%s.csv" %(i)) as csv_file_r:
            csv_reader = csv.reader(csv_file_r, delimiter=',')
            line_count = 1

            for row in csv_reader:
                if row[0] == "pink morsel":
                    price = row[1][1:]
                    sales = float(price)*float(row[2])
                    writer.writerow({'Sales': sales, 'Date': row[3], 'Region': row[4]})

                line_count += 1
