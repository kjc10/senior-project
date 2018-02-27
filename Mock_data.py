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
import csv

#Amount of data that we will need, should be 2112 
num = 2112

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
hoodMajor = ["MJBSCS", "MJBAMATH", "MJBABIOL", "MJBACHEM", "MJBAENG", "MJBAHIST", "MJBAPSY", "MJBAPHIL", "MJBAPSCI", "MJBAECON", "MJMSCS", "MJMSBIFX", "MJMSCOUN", "MJMSCYBR", "MJMSIT"]

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

#creates array for roles. All are NULL
sRole = []

#creats array for Advisor ID
AdvPIDs = []

#creates array for Advisors last names
AdvLast = []

#creates array for Advisors first names
AdvFirst = []

#creates array for Advisores usernames
AdvUsernames = []

#creates array for advisors
Advisors = []

#creates array for advisor email
AdvEmails = [] 

#creates an array to use for advisors in students
StudentAdvisors = []
StudentAdvisorsEmail = []

#Create advisors/instructors 251
for i in range(251):
    #Advisor IDs
    Advid = scribe_data.numerify(text="######")
    Advid = "P000" + Advid
    #Makes sure there aren't any duplicates
    while Advid in AdvPIDs:
        Advid = scribe_data.numerify(text="######")
        Advid = "P000" + Advid
    while Advid in pstuList:
        dvid = scribe_data.numerify(text="######")
        Advid = "P000" + Advid
    AdvPIDs.append(Advid)
    #Advisor last name
    adlastname = scribe_data.last_name()
    while adlastname in AdvLast:
        adlastname = scribe_data.last_name()
    AdvLast.append(adlastname)
    #Advisor first name
    adfirstname = scribe_data.first_name()
    AdvFirst.append(adfirstname)
    #Advisors full names
    advisors_full_name = adfirstname + " " + adlastname
    Advisors.append(advisors_full_name)
    #Advisor username
    adusername = adlastname.lower()
    AdvUsernames.append(adusername)
    #Advisor email
    adEmail = adusername + "@hood.edu"
    AdvEmails.append(adEmail)

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
    #Gender field of Yes or No
    gender = scribe_data.boolean(chance_of_getting_true=37)
    if gender == True:
        gender = "Yes"
    elif gender == False:
        gender = "No"
    sGender.append(gender)
    if gender == "Yes":
        #first name
        firstname = scribe_data.first_name_male()
        #middle name
        middlename = scribe_data.first_name_male()
    elif gender == "No":
        #first name
        firstname = scribe_data.first_name_female()
        #middle name
        middlename = scribe_data.first_name_female()
    firstN.append(firstname)
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
    #Majors
    randNum = random.randint(0, 14)
    major = hoodMajor[randNum]
    sMajors.append(major)
    #Athlete
    athlete = scribe_data.boolean(chance_of_getting_true=15)
    if athlete == True:
        athlete = "Yes Athlete"
    elif athlete == False:
        athlete = "NULL"
    sAthlete.append(athlete)
    #Advisors and their emails
    randNum = random.randint(0, 250)
    ad = Advisors[randNum]
    ademail = AdvEmails[randNum]
    while StudentAdvisors.count(Advisors[randNum]) == 15:
        randNum = random.randint(0, 250)
        ad = Advisors[randNum]
        ademail = AdvEmails[randNum]
    StudentAdvisors.append(ad)
    StudentAdvisorsEmail.append(ademail)
    #Roles
    sRole.append("NULL")
    
 
       
#Grad or Undergrad field of U (1128) or G (984) 
for i in range(1128):
    grad = "U"
    sGrad.append(grad)
for i in range(984):
    grad = "G"
    sGrad.append(grad)
    
#Visa 20 undergrads are visa and 132 grad are visa
for i in range(20):
    uvisa = "Visa"
    sVisa.append(uvisa)
for i in range(1108):
    uvisa = "NULL"
    sVisa.append(uvisa)
for i in range(132):
    uvisa = "Visa"
    sVisa.append(uvisa)
for i in range(852):
    uvisa = "NULL"
    sVisa.append(uvisa)

#class
for i in range(282):
    studClass = "FR"
    sClass.append(studClass)
for i in range(214):
    studClass = "SP"
    sClass.append(studClass)
for i in range(289):
    studClass = "JR"
    sClass.append(studClass)
for i in range(323):
    studClass = "SR"
    sClass.append(studClass)
for i in range(20):
    studClass = "OTHER"
    sClass.append(studClass)
for i in range(984):
    studClass = "NULL"
    sClass.append(studClass)

#Matric Term
for i in range(num):
    matricyear = scribe_data.year()
    while int(matricyear) < 2012:
        matricyear = scribe_data.year()
    semester = scribe_data.boolean(chance_of_getting_true=70)
    if semester == True:
        semester = "FALL"
    elif semester == False:
        semester = "SPRING"
    matric = matricyear + "/" + semester
    matricTerm.append(matric)
    
#Credits for full time students
for i in range(1962):
    full_studcredits = random.randint(12, 18)
    sCredits.append(full_studcredits)
#Credits 150 of them are part time
for i in range(150):
    part_studcredits = random.randint(0, 11)
    sCredits.append(part_studcredits)

#path to where the CSV file will be stored
path = "C:\\Users\\karen\\Documents\\student.csv"

#Open the CSV file to write in the data
file = open(path, 'w')
writer = csv.writer(file)

#Insert all the data into the CSV file
for i in range(2112):
    studid = stuList[i]
    pid = pstuList[i]
    last = lastN[i]
    first = firstN[i]
    middle = middleN[i]
    street = streetA[i]
    city = cityA[i]
    state = stateA[i]
    zipcode = zipA[i]
    stuEmail = sEmail[i]
    birth = sBirthdate[i]
    phone = sPhone[i]
    gender = sGender[i]
    username = sUsername[i]
    graduate = sGrad[i]
    major = sMajors[i]
    studclass = sClass[i]
    matric = matricTerm[i]
    credit = sCredits[i]
    athlete = sAthlete[i]
    visa = sVisa[i]
    advisor = StudentAdvisors[i]
    advisoremail = StudentAdvisorsEmail[i]
    writer.writerow([studid, pid, last, first, middle, street, city, state, zipcode, stuEmail, birth, phone, gender, username, graduate, major, studclass, matric, credit, athlete, visa, advisor, advisoremail])
    
#Close the CSV file
file.close()  