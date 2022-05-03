from masseges import *
import csv
from time import sleep
DS = Masseges()

with open('words_for_discord.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        DS.ds.append(list(row.values())[0])
print(DS.ds)
#for i in range(len(DS.ds)):
    #sleep(3)
    #print(DS.ds[i])


"""
#ds = []
#print(row.values)
        #ds.append(list(row.values())[0])
#print(ds)
"""