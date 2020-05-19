# DO NOT INCLUDE IN SPRINT CHALLENGE!

# This reads the big US Cities CSV and filters it down to cities with population
# >= 750,000. Also strips a bunch of columns.

import csv

with open('uscitiesv1.4.csv', newline='') as csvin, open('cities.csv', 'w', newline='') as csvout:
    reader = csv.reader(csvin)
    writer = csv.writer(csvout)

    first = True
    for row in reader:
        del row[15] # ID
        del row[12] # incorporated
        del row[11] # source
        del row[9] # population_proper
        del row[4] # county fips
        del row[2] # state ID
        del row[1] # city_ascii
        if first:
            writer.writerow(row)
            first = False
        else:
            if row[5] == '':
                continue
            pop = int(float(row[5]))
            row[5] = pop
            if pop >= 750000:
                writer.writerow(row)

