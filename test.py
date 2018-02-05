# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:27:42 2018

@author: karen
"""

from faker import Faker
fake_data = Faker()

studid = fake_data.numerify(text="######")
studid = "000" + studid
print("Student ID:")
print(studid)
print(" ")

pid = "P" + studid
print("People ID")
print(pid)
print(" ")

lastname = fake_data.last_name()
print("Last Name")
print(lastname)
print(" ")

firstname = fake_data.first_name()
print("First Name")
print(firstname)
print(" ")

middlename = fake_data.first_name()
print("Middle Name")
print(middlename)
print(" ")

street_address = fake_data.street_address() 
print("Street Address")
print(street_address)
print(" ")

city = fake_data.city()
print("City")
print(city)
print(" ")

state = fake_data.state_abbr()
print("State")
print(state)
print(" ")

zipcode = fake_data.zipcode_plus4()
print("Zipcode")
print(zipcode)
print(" ")

email = fake_data.ascii_safe_email()
print("Email")
print(email)
print(" ")

birthmonth = fake_data.month()
birthday = fake_data.day_of_month()
birthyear = fake_data.year()
birthdate = birthmonth + "/" + birthday + "/" + birthyear
print("Birthdate")
print(birthdate)
print(" ")

phonenumber = fake_data.numerify(text="##########")
print("Phone number")
print(phonenumber)
print(" ")

username = email.split("@")
username = username[0]
print("Username")
print(username)
print(" ")

advisor = fake_data.name()
print("Advisor")
print(advisor)
print(" ")

ademail = fake_data.ascii_safe_email()
print("Advisor Email")
print(ademail)
print(" ")
