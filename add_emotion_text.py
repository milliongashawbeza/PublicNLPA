import csv
import random

var2 = random.randint(10**12, 10**13 - 1)
# randint is inclusive on both sides, so we need the - 1

# or


def add_dataset(s1,s2):
    with open('test_emotion.csv', mode='w') as ds:
        ds_writer = csv.writer(ds, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ds_writer.writerow(['test', s2, '99'])
        return True





