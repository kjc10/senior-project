# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 21:31:30 2018

@author: Karen J Canas Hernandez

This program will develop mock data using the python faker library for our senior project: 
Web-enabled Repository & Note-taker Scheduling System

Copyright (c) 2017 Karen J Canas Hernandez, Jacob W. Denion, Afton J. Woodring

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
"""
#Imports Faker Library
from faker import Faker
#Creates Faker instance
scribe_data = Faker()
#For random numbers in email
import random
#Imports csv to create csv files
#import csv

#Amount of data that we will need, 
num = 10

#Creates array to store all the student IDs
stuList = []
#Creates array to store all the PIDs
pstuList = []

#Creates array to store all the last names
lastN = []

#Creates array to store all the first names
firstN = []

#Creates array to store all the middle names
middleN = []

#Creates array to store all the street addresses
streetA = []

#Creates array to store all the cities
cityA = []

#States list to make sure that accurate data is presented for states
realStates = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN","IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI","SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

#Creates array to store all states
stateA = []

#creates array to store all zipcodes
zipA = []

#creates array to store all student emails
sEmail = []

#creates array to store all birthdates
sBirthdate = []

#creates array to store all phone numbers
sPhone = []

#creates array to store gender Yes or No fields
sGender = []

#creates array to store username
sUsername = []

#creates array to store grad or undergrad field with U or G
sGrad = []

#List of real majors at hood
hoodMajor = []

#creates an array to store majors of fake data
sMajors = []

#creates array to store the class "FR, SP, JR, SR"
sClass = []

#creates array for the matric term
matricTerm = []

#creates array for the credits
sCredits = []

#creates array for the athelete question
sAthlete = []

#creates array for the visa question
sVisa = []

#creates array for advisors
sAdvisor = []

#creates array for advisor email
sAdEmail = [] 

#Develops all the fake fields for the database
for i in range(num):
    #IDs
    studid = scribe_data.numerify(text="######")
    studid = "000" + studid
    #Makes sure there aren't any duplicates
    while studid in stuList:
        studid = scribe_data.numerify(text="######")
        studid = "000" + studid
    stuList.append(studid)
    #PIDs
    pid = "P" + studid
    pstuList.append(pid)
    #last name
    lastname = scribe_data.last_name()
    lastN.append(lastname)
    #first name
    firstname = scribe_data.first_name()
    firstN.append(firstname)
    #middle name
    middlename = scribe_data.first_name()
    middleN.append(middlename)
    #street address
    street = scribe_data.street_address()
    streetA.append(street)
    #city
    city = scribe_data.city()
    cityA.append(city)
    #state
    state = scribe_data.state_abbr()
    #makes sure it is a real state
    while state not in realStates:
        state = scribe_data.state_abbr()
    stateA.append(state)
    #zip code
    zipcode = scribe_data.zipcode_plus4()
    zipA.append(zipcode)
    #username
    username = firstN[i][0].lower() + middleN[i][0].lower() + lastN[i][0].lower()
    sUsername.append(username)
    #email
    randNum = random.randint(0, 99)
    studEmail = username + str(randNum) + "@hood.edu"
    while studEmail in sEmail:
        randNum = random.randint(0, 99)
        studEmail = username + str(randNum) + "@hood.edu"
    sEmail.append(studEmail)
    #birthday
    birthmonth = scribe_data.month()
    birthday = scribe_data.day_of_month()
    birthyear = scribe_data.year()
    #makes sure students are not less than 17 years old
    while int(birthyear) > 2000:
        birthyear = scribe_data.year()
    birthdate = birthmonth + "/" + birthday + "/" + birthyear
    sBirthdate.append(birthdate)
    #Phone number
    phonenumber = scribe_data.numerify(text="##########")
    while phonenumber in sPhone:
        phonenumber = scribe_data.numerify(text="##########")
    sPhone.append(phonenumber)
    #Gender field of Yes or No
    gender = scribe_data.boolean()
    if gender == True:
        gender = "Yes"
    elif gender == False:
        gender = "No"
    sGender.append(gender)
    #Grad or Undergrad field of U or G
    grad = scribe_data.boolean()
    if grad == True:
        grad = "U"
    elif grad == False:
        grad = "G"
    sGrad.append(grad)
    #Majors
    #Class
    randClass = random.randint(1, 4)
    if randClass == 1:
        studClass = "FR"
    elif randClass == 2:
        studClass = "SP"
    elif randClass == 3:
        studClass = "JR"
    elif randClass == 4:
        studClass = "SR"
    sClass.append(studClass)
    #Matric Term
    #Credits
    #Athlete
    #Visa
    #Advisor Name
    #Advisor Email
    
    
for i in range(num):
    print(sClass[i])
    
'''
#path to where the CSV file will be stored
path = "C:\\Users\\karen\\Documents\\student.csv"

#Open the CSV file to write in the data
file = open(path, 'w')
writer = csv.writer(file)

#Insert all the data into the CSV file
for i in range(10):
    studid = stuList[i]
    pid = pstuList[i]
    writer.writerow([studid, pid])
    
#Close the CSV file
file.close()
'''    