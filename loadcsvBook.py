# import csv
# from faker import Faker

# fileName = open('dataBook.csv','w')
# fileWriter = csv.writer(fileName)
# header = ['name','age']
# fileWriter.writerow(header)


import csv 
from faker import Faker 
import logging
logging.basicConfig(level=logging.INFO)

# output = open('dataBook.csv', 'w',newline='')
# fileWriter = csv.writer(output)

# fake = Faker()
# header = ['name', 'profession','contact']
# fileWriter.writerow(header)
# for i in range(1000):
#     fileWriter.writerow([fake.name(), fake.job(), fake.phone_number()])


num_records = int(input("Enter the number of records to generate: "))


with open('dataBook.csv','w') as output:
    filewriter = csv.writer(output)
    fake = Faker('en_IN')
    header = ['name', 'profession', 'contact', 'email', 'address']
    filewriter.writerow(header)
    for i in range(num_records):
        filewriter.writerow([fake.name(),fake.job(),fake.phone_number(),fake.email(), fake.address()])
        if i % 100 ==0:
            logging.info(f'{i} rows written.')




# Useful Applications of the Data 
# Database Import 
# Web Application Testing 
# Data Analysis Practice 
# Machine Learning 
# Data Validation 
# CSV Transformation
# Generate Large Datasets 
# Visualization 
# API Testing 
# Generate Data for Specific Scenarios 
