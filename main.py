from faker import Faker
import pandas as pd
print("Choose region ")
print("Enter 1 for INDIA")
print("Enter 2 for INDONESIA")
print("Enter 3 for RUSSIA")
print("Enter 4 for JAPAN")
print("Enter 5 for UNITED STATE")
print("Enter 6 for CHINA")
try:
    region=int(input("enter region : "))
except ValueError:
    print("Choose a valid region")
    exit()
try:
    enter=int(input("Enter how much rows you want : "))
except ValueError:
    print("Please enter a valid whole number")
    exit()
if enter <=0:
    print("Please enter a positive value")
    exit()
regions={
    1:"en_IN",
    2:"id_ID",
    3:"ru_RU",
    4:"ja_JP",
    5:"en_US",
    6:"zh_CN"
}
if region  not in regions:
    print("Invalid region!")
    exit()
else:
    i=regions[region]
    fake=Faker(i)
data={
    "Name":[fake.name() for i in range(enter)],
    "Mail":[fake.email() for i in range(enter)],
    "Phone no":[fake.phone_number() for i in range(enter)],
    "Region":[fake.current_country() for i in range(enter)],
    "City":[fake.city() for i in range(enter)],
    "Address":[fake.address() for i in range(enter)],
    "Company":[fake.company() for i in range(enter)],
    "Job":[fake.job() for i in range(enter)]
}
df=pd.DataFrame(data)
df.to_excel("fake_data.xlsx",index=False)
print("Data save successfully!")
