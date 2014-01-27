import csv

train = open('resource/train-remapped.csv', 'rb')
train_1000 = open('resource/my_train.csv', 'wb')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
count = 0
for row in train:
    row = row.replace(', ', ',')
    train_1000.write(row)
    count += 1
    if count == 1:
        break
    