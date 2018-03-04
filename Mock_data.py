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
num = 150

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

#creates an array to use for emails
StudentAdvisorsEmail = []

#List of real course codes
coursesCode = ['AFAM 251 01', 'AFHS 251 01', 'AFPS 240 01', 'ANTH 201 01','ARAB 102 01', 'ARAB 105 01', 'ARAB 202 01', 'ARLS 354 01', 'ART 213 01', 'ART 220 01', 'ART 221 01', 'ART 250 01', 'ART 299G 01', 'ART 306 01', 'ART 308 01','ART 331B 01','ART 360 01', 'ARTS 564 01', 'ASL 101 01', 'ASL 102 01','BIFX 501 01', 'BIFX 545 01', 'BIFX 546 01', 'BIFX 547 01', 'BIFX 550 01', 'BIFX 551 01']

#List of all Hood course titles
coursesTitle = ['The African Diaspora', 'Race and Racism in the United States','African American Politics', 'Introduction to Anthropology', 'Elementary Arabic II', 'Arabic Conversation','Intermediate Arabic II','Mesoamerican Art and Archaeology', 'Art, History, and Humanities', 'History of Art I', 'History of Art II', 'Art of Asia', 'Special Topic: Art of Three Faiths', 'Writing for Art and Archaeology', 'Myths, Saints, and Symbols', 'Mus, Sites,Cities: Castles/Crowns-Eng/Scot', 'Nineteenth Century Art', 'Aesthetics and Criticism', 'American Sign Language I', 'American Sign Language II', 'Foundation in Life Sciences', 'Leadership Skills/Proj Mgmt in Life Science', 'Knowledge Reasoning/Machine Learning', 'Web-based BIFX & Apps in Life Sciences', 'Nucleic Acid Seq Analy/Protein Modeling', 'Programming for Bioinformatics']

#array for fake courses code
mock_coursecode = []

#array for fake course titles
mock_coursetitle = []

#array for students pid associated with courses
course_pid = []

#array that creates instructors
prof_pid = []
prof_first = []
prof_last = []
prof_email= []
prof_username = []


#Create advisors/instructors 251
for i in range(18):
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
    randNum = random.randint(0, 17)
    ad = Advisors[randNum]
    ademail = AdvEmails[randNum]
    StudentAdvisors.append(ad)
    StudentAdvisorsEmail.append(ademail)
    #Roles
    sRole.append("NULL")
    
 
       
#Grad or Undergrad field of U (1128) or G (984) 
for i in range(80):
    grad = "U"
    sGrad.append(grad)
for i in range(70):
    grad = "G"
    sGrad.append(grad)
    
#Visa 20 undergrads are visa and 132 grad are visa
for i in range(2):
    uvisa = "Visa"
    sVisa.append(uvisa)
for i in range(78):
    uvisa = "NULL"
    sVisa.append(uvisa)
for i in range(10):
    uvisa = "Visa"
    sVisa.append(uvisa)
for i in range(60):
    uvisa = "NULL"
    sVisa.append(uvisa)

#class
for i in range(37):
    studClass = "FR"
    sClass.append(studClass)
for i in range(29):
    studClass = "SP"
    sClass.append(studClass)
for i in range(39):
    studClass = "JR"
    sClass.append(studClass)
for i in range(43):
    studClass = "SR"
    sClass.append(studClass)
for i in range(2):
    studClass = "OTHER"
    sClass.append(studClass)
for i in range(70):
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
for i in range(139):
    full_studcredits = random.randint(12, 18)
    sCredits.append(full_studcredits)
#Credits 150 of them are part time
for i in range(11):
    part_studcredits = random.randint(1, 11)
    sCredits.append(part_studcredits)
#Professors with courses    
for j in range(len(coursesCode)):
    rand = random.randint(0, 17)
    professor_pid = AdvPIDs[rand]
    professor_first = AdvFirst[rand]
    professor_last = AdvLast[rand]
    professor_email = AdvEmails[rand]
    professor_username = AdvUsernames[rand]
    while prof_pid.count(AdvPIDs[rand]) == 2:
        rand = random.randint(0, 17)
        professor_pid = AdvPIDs[rand]
        professor_first = AdvFirst[rand]
        professor_last = AdvLast[rand]
        professor_email = AdvEmails[rand]
        professor_username = AdvUsernames[rand]
    prof_pid.append(professor_pid)
    prof_first.append(professor_first)
    prof_last.append(professor_last)
    prof_email.append(professor_email)
    prof_username.append(professor_username)   
    

for i in range(num):
    student_course_pid = pstuList[i]
    #if they are part time
    if sCredits[i] < 12:
        randNum = random.randint(1, 3)
        while randNum > 0:
            temp = random.randint(0, 25)
            curr_coursecode = coursesCode[temp]
            curr_coursetitle = coursesTitle[temp]
            mock_coursecode.append(curr_coursecode)
            mock_coursetitle.append(curr_coursetitle)
            course_pid.append(student_course_pid)
            randNum = randNum - 1
    #if they are full time
    elif sCredits[i] > 11:
        randNum = random.randint(4, 5)
        while randNum > 0:
            temp = random.randint(0, 25)
            curr_coursecode = coursesCode[temp]
            curr_coursetitle = coursesTitle[temp]
            mock_coursecode.append(curr_coursecode)
            mock_coursetitle.append(curr_coursetitle)
            course_pid.append(student_course_pid)
            randNum = randNum - 1     
   


#path to where the student CSV file will be stored
path = "C:\\Users\\karen\\Documents\\student.csv"
second_path = "C:\\Users\\karen\\Documents\\courses.csv"


#Open the CSV file to write in the data
file = open(path, 'w')
writer = csv.writer(file)

#Insert all the data into the CSV file
for i in range(num):
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

second_file = open(second_path, 'w')
second_writer = csv.writer(second_file)

#Insert all the data into the CSV file
for i in range(len(mock_coursecode)):
    coursepid = course_pid[i]
    coursesubj = mock_coursecode[i]
    coursetitle = mock_coursetitle[i]
    courseterm = "20182"
    ind = coursesCode.index(coursesubj)
    profssor_id = prof_pid[ind]
    profssor_first = prof_first[ind]
    profssor_last = prof_last[ind]
    profssor_email = prof_email[ind]
    profssor_user = prof_username[ind]
    grades = "NULL"
    second_writer.writerow([coursepid, coursesubj, coursetitle, courseterm, profssor_id, profssor_first, profssor_last, profssor_email, profssor_user, grades])
    
#Close the CSV file
second_file.close()