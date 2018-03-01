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

#List of real course codes
coursesCode = ['AFAM 251 01', 'AFHS 251 01', 'AFPS 240 01', 'ANTH 201 01','ARAB 102 01', 'ARAB 105 01', 'ARAB 202 01', 'ARLS 354 01', 'ART 213 01', 'ART 220 01', 'ART 221 01', 'ART 250 01', 'ART 299G 01', 'ART 306 01', 'ART 308 01','ART 331B 01','ART 360 01', 'ARTS 564 01', 'ASL 101 01', 'ASL 102 01','BIFX 501 01', 'BIFX 545 01', 'BIFX 546 01', 'BIFX 547 01', 'BIFX 550 01', 'BIFX 551 01', 'BFIX 553 01', 'BIOL 111 01', 'BIOL 112 01', 'BIOL 113 01', 'BIO 117 01', 'BIO 134 01', 'BIOL 138 01','BIOL 141 01','BIOL 201 01','BIOL 203 01','BIOL 204 01','BIOL 232 01', 'BIOL 316 01','BIOL 331 01','BIOL 344 01', 'BIOL 408 01', 'BIOL 424 01', 'BIOL 428 01', 'BMS 501 01','BMS 524 01', 'BMS 528 01','BMS 533 01','CAMG 330','CHEM 210 01','CHEM 324 01','CHEM 402 01','CHEM 432 01','CJ 230 01','CL 202 01','CMA 200 01','CMA 201 01','CMA 204 01','CMA 207 01','CMA 280 01','CMA 281 01','CMA 305 01','CMA 306 01','CMA 310 01','CMA 313 01','CMA 411 01','COUN 501 01', 'COUN 502 01','COUN 502L 01','COUN 504 01','COUN 505 01','COUN 511 01','COUN 523 01','COUN 528 01','COUN 531 01','COUN 533 01','COUN 543 01', 'COUN 554 01', 'COUN 556 01','COUN 599B 01','COUN 599C 01','COUN 599D 01','CS 112 01','CS 201 01','CS 202 01','CS 219 01','CS 226 01','CS 319 01','CS 329 01','CS 443 01','CS 450 01','CS 464 01','CS 508 01','CS 519 01','CS 520 01','CS 543 01','CS 550 01','CS 564 01','CS 565 01','CSIT 302 01','CSIT 532 01','CSIT 537 01','CSIT 555 01','CSIT 565 01','CYBR 521 01','CYBR 532 01','CYBR 537 01','CYBR 548 01','CYBR 555 01','CYBR 560 01','EAP 500 01','ECMG 212 01','ECMG 303 01','ECMG 478 01','ECMG 578 01','ECON 205 01','ECON 206 01','ECON 206 02','ECON 306 01','ECON 306 02','ECON 309 01','ECON 328 01','ECON 410 01','ECON 560 01','ECPS 414 01','ECPS 514 01','EDUC 204 01','EDUC 223 01','EDUC 224 01','EDUC 236 01','EDUC 308 01','EDUC 316 01','EDUC 317 01','EDUC 320 01','EDUC 321 01','EDUC 324 01','EDUC 330 01','EDUC 340 01','EDUC 347 01','EDUC 353 01','EDUC 354 01','EDUC 360 01','EDUC 373 01','EDUC 412 01','EDUC 445 01','EDUC 502 01','EDUC 502B 01','EDUC 502W 01','EDUC 514 01','EDUC 514B','EDUC 514M 01','EDUC 519 01','EDUC 520 01','EDUC 523 01','EDUC 524 01','EDUC 542 01','EDUC 546 01','EDUC 553 01','EDUC 561 01','EDUC 577 01','EDUC 577B 01','EDUC 577W 01','EDUC 581 01','EDUC 581B 01','EDUC 581M 01','EDUC 582 01', 'EDUC 582B 01','EDUC 582M 01','EDUC 583 01','EDUC 583M 01','EDUC 583M 03','EDUC 586 01','EDUC 586M 04','EDUC 586W 01','EDUC 595 01','ENGL 099 01','ENGL 100 01','ENGL 100 02','ENGL 100 03','ENGL 100 04','ENGL 100 05','ENGL 136 01','ENGL 136 02','ENGL 138 01','ENGL 210 01','ENGL 223 01','ENGL 250 01','ENGL 252 01','ENGL 269 01','ENGL 272 01','ENGL 278 01','ENGL 282 01','ENGL 299I 01','ENGL 313 01','ENGL 397B 01','ENGL 410 01','ENSP 101 01','ENSP 103 01','ENSP 397A 01','ENSP 403 01','ENSP 407 01','ENTH 205 01','ENV 503 01','ENV 503G 01','ENV 505 01','ENV 507 01','ENV 507G 01','ENV 563 01','ENV 563G 01','FREN 105 01','GER 105 01','GER 207 01','GER 208 01','GERO 554 01','GERO 556 01','GLBS 345 01','GNST 220 01','HIST 202 01','HIST 217 01','HIST 218 01','HIST 218 02','HIST 264 01','HIST 265 01','HIST 266 01','HIST 268 01','HIST 373 01','HIST 378 01','HIST381 01','HIST 397A 01','HIST 397B 01','HON 102 01','HON 102 02','HON 102 03','HON 315 01','HON 322 01','IT 180 01','IT 280 01','IT 510 01','IT 512 01','IT 514 01','IT 521 01','IT 530 01','IT 548 01','ITMG 388 01','ITMG 516 01','ITMG 524 01','ITMG 533 01','LEAD 621 01','LEAD 699A 01', 'LSSP 240 01','LWPS 230 01','MATH 107 01','MATH 11A 01','MATH 11B 01','MATH 112 01','MATH 112 02','MATH 112 03','MATH 120 01','MATH 120L 01','MATH 207 01','MATH 213 01','MATH 320 01','MATH 440 01','MATH 502 01','MEST 300 01','MGMT 205 01','MGMT 205 02','MGMT 281 01','MGMT 284 01','MGMT 284 02','MGMT 301 01','MGMT 306 01','MGMT 307 01','MGMT 312 01','MGMT 314 01','MGMT 322 01','MGMT 331 01','MGMT 410 01','MGMT 423 01','MGMT 424 01','MGMT 424 02','MGMT 433 01','MGMT 454 01','MGMT 553 01','MGMT 554 01','MGMT 560 01','MGMT 561 01','MGMT 563 01','MGMT 565 01','MGMT 567 01','MGMT 569 01','MGMT 569L 01','MGMT 571 01','MGMT 577 01','MGMT 581 01','MGMT 585 01','MGMT 590 01','MGMT 590L 01','MGMT 699A 01','MUSC 100 01','MUSC 103 01','MUSC 103 02','NUR 203 01','NUR 205 01','NUR 303 01','NUR 304 01','NUR 309 01','NUR 320 01','NUR 404 01','PHIL 200 01','PHIL 200 02','PHIL 203 01','PHIL 221 01','PHIL 221 02','PHIL 315 01','PHYS 102 01','PHYS 204 01','PHYS 324 01','PHYS 432 01','PLRL 306 01','PSCI 205 01','PSCI 210 01','PSCI 302 01','PSCI 303 01','PSCI 313 01','PSCI 336 01','PSY 101 01','PSY 101 02','PSY 204 01','PSY 205 01','PSY 239 01','PSY 301 01','PSY 315 01','PSY 315 02','PSY 373 01','PSY 418 01','PSY 431 01','PSY 441 01','PSY 456 01','PSY 505 01','PSY 511 01','PSY 531 01','REL 200 01','SOC 101 01','SOC 101 02','SOC 259 01','SOC 260 01','SOC 261 01','SOC 300 01','SOC 308 01','SOWK 214 01','SOWK 301 01','SOWK 302 01','SOWK 320 01','SOWK 342 01','SPAN 105 01','SPAN 208 01','SPAN 323 01','THAN 523 01','THAN 528 01','THAN 529 01','THEA 101 01','THEA 202 01', 'BIOL 434 01', 'BIOL 437 01', 'BMS 527 01', 'BMS 534 01', 'BMS 537 01', 'CHEM 100 01', 'CHEM 102 01', 'CHEM 102 02', 'CHEM 102 03', 'COUN 534 01', 'EDUC 323 01', 'ENGL 219 01', 'ENGL 319 01', 'FREN 102 01', 'FREN 102 02', 'FREN 202 01', 'GER 102 01', 'GER 202 01', 'GNST 101 01', 'GNST 101 02', 'GNST 101 03', 'GNST 101 04', 'GNST 101 05', 'MATH 098 01', 'MATH 098 02', 'MATH 099 01', 'MATH 099 02', 'MATH 201 01', 'MATH 202 01', 'MSCI 102 01', 'MSCI 202 01', 'MSCI 302 01', 'MSCI 402 01', 'MUSC 101 01', 'NUR 307 01', 'NUR 308 01', 'PE 214 01', 'PE 225 01', 'PE 225 02', 'PE 228 01', 'PE 228 02', 'PE 250 01', 'PSY 211 01', 'PSY 434 01', 'PSY 534 01', 'SPAN 102 01', 'SPAN 102 02', 'SPAN 102 03', 'SPAN 102 04', 'SPAN 102 05', 'SPAN 202 01', 'SPAN 202 02', 'SPAN 202 03', 'BIOL 111 01',  'BIOL 111 02', 'BIOL 112 01', 'BIOL 113 01', 'BIOL 113 02', 'BIOL 117 01', 'BIOL 201 01', 'BIOL 201 02', 'BIOL 201 03', 'BIOL 203 01', 'BIOL 203 02', 'BIOL 203 03', 'BIOL 204 01', 'BIOL 204 02', 'BIOL 232 01', 'BIOL 316 01', 'BIOL 331 01', 'BIOL 344 01', 'BIOL 344 02', 'BIOL 408 01', 'CHEM 210 01', 'CHEM 210 02', 'CHEM 324 01', 'CHEM 403 01', 'CHEM 434 01', 'EDUC 223 01', 'EDUC 223 02', 'EDUC 223 03', 'EDUC 224 01', 'EDUC 224 02', 'EDUC 224 03', 'EDUC 324 01', 'EDUC 324 02', 'EDUC 324 03', 'ENSP 102 01', 'ENSP 103 01', 'ENV 524A 01', 'ENV 526G 01', 'ENV 526H 01', 'NUR 205 01', 'NUR 205 02', 'NUR 205 03', 'NUR 205 04', 'NUR 303 01', 'PHYS 102 01', 'PHYS 204 01', 'PHYS 434 01', 'ACRA 322 01', 'ART 322 01', 'ARTS 101 01', 'ARTS 203 01', 'ARTS 203 02', 'ARTS 203 03', 'ARTS 211 01', 'ARTS 224 01', 'ARTS 234 01', 'ARTS 237 01', 'ARTS 243 01', 'ARTS 314 01', 'ARTS 316O 01',  'ARTS 324 01', 'ARTS 334 01', 'ARTS 343 01', 'ARTS 344 01', 'ARTS 345 01', 'ARTS 505 01', 'ARTS 507 01', 'ARTS 510 01', 'ARTS 520 01', 'ARTS 525 01', 'ARTS 531 01', 'ARTS 540 01', 'ARTS 545 01', 'ARTS 574 01', 'CMA 226 01', 'CMA 246 01', 'CMA 302 01', 'CMA 322 01', 'CMA 337 01', 'CMA 402 01', 'ART 470 01', 'ART 570 01', 'ARTS 470 01', 'ARTS 570 01', 'BIOL 470 01', 'BMS 570 01', 'BMS 571 01', 'CHEM 270 01', 'CMA 470 01', 'CS 475 01', 'ECON 470 01', 'EDUC 401 01', 'EDUC 460 01', 'ENGL 470 01', 'FREN 470 01', 'FYS 101 01', 'GLBS 470 01', 'HON 470 01', 'HON 470 02', 'IMC 470 01', 'LEAD 602 01', 'LEAD 630 01', 'MATH 471 01', 'MGMT 411 01', 'MGMT 411 02', 'MUSC 474 01', 'MUSC 475 01', 'NUR 470 01', 'PHYS 270 01', 'PLRL 501 01', 'PSCI 399C 01', 'PSCI 470 01', 'PSY 370A 01', 'SOC 470 01', 'SOWK 446B 01', 'SOWK 452 01']

#List of all Hood course titles
coursesTitle = ['The African Diaspora', 'Race and Racism in the United States','African American Politics', 'Introduction to Anthropology', 'Elementary Arabic II', 'Arabic Conversation','Intermediate Arabic II','Mesoamerican Art and Archaeology', 'Art, History, and Humanities', 'History of Art I', 'History of Art II', 'Art of Asia', 'Special Topic: Art of Three Faiths', 'Writing for Art and Archaeology', 'Myths, Saints, and Symbols', 'Mus, Sites,Cities: Castles/Crowns-Eng/Scot', 'Nineteenth Century Art', 'Aesthetics and Criticism', 'American Sign Language I', 'American Sign Language II', 'Foundation in Life Sciences', 'Leadership Skills/Proj Mgmt in Life Science', 'Knowledge Reasoning/Machine Learning', 'Web-based BIFX & Apps in Life Sciences', 'Nucleic Acid Seq Analy/Protein Modeling', 'Programming for Bioinformatics', 'Bioinformatics Applications II', 'Secret Lives of Plants', 'Biology of Food & Nutrition', 'Newsstand Biology','This Course Will Bug You', 'The Biology of Cancer', 'The Human Health Mosaic','Thinking About Thinking', 'Evolution and Ecology', 'Intro to Cell Biology & Genetics','Anatomy & Physiology for Nurses II', 'Microbiology for Nurses', 'Genetics', 'Microbiology', 'Ornithology', 'Adv Human Anatomy and Physiology', 'Molecular Biology Eukaryotic Cells', 'Immunology', 'Foundations in Life Sciences', 'Molecular Biology Eukaryotic Cells', 'Immunology', 'Medical Virology','Social Media', 'Organic Chemistry II','Instrumental Methods of Analysis','Biological Chemistry II','Thermodynamics & Statistical Mechanics','Introduction to Criminal Justice','Mythology','Mass Media and Society','News Writing','Media History','Principles of Speech Communication','Screen Craft','Introduction to Screenwriting','Communications Law','Business Writing in the Digital Age','Public Relations','	Writing for Public Relations','Public Relations Campaigns','Prof, Legal & Ethical Responsibilities','Social & Cultural Foundations of Couns','Social & Cultural Foundations of Couns','Counseling Techniques','Group Dynamics,Proc & Counseling','Theory and Principles of Counseling','Principles of Thanatology','Developmental Perspectives:Thanatology','Diagnosis & Psychopathology', 'Marriage and Family Counseling', 'Counseling Youth','Social Gerontology', 'Health and Aging','Foundations in Play Therapy', 'Foundations in Disaster Mental Health','Affirmative Therapy w/ LGBTQIA+ Client','Introduction to Computer Music','Computer Science I','Computer Science II','Advanced Data Structures','Computer Organization and Design','Algorithm Analysis','Intro to Database Management Systems','Machine Learning','Digital Logic and Switching Theory','Operating Systems','Computer Organization and Design','Advanced Data Structures','Algorithm Analysis','Machine Learning','Digital Logic and Switching Theory','Operating Systems','Database System Concepts','Impact of Computers on Society','Computer Forensics','Applied Encryption and Cryptology','Info Systems Security','Advanced Database Management Systems','Info Assurance & Risk Assessment','Computer Forensics','Applied Encryption and Cryptology','Telecommunications & Networking','Information Systems Security','Cybersecurity Capstone','Advanced English for Academic Purposes','Statistics for Economics & Management','Principles of Finance & Investment','International Financial Management','International Financial Management','Princ of Macroeconomics','Princ of Macroeconomics','Princ of Macroeconomics','Microeconomic Analysis','Microeconomic Analysis','Monetary Policy & Financial Markets','Labor Economics','Public Economics','Managerial Economics','Environmental Policy','Environmental Policy','Foundations of Educ in a Diverse Society','Child Development','Processes & Acquisition of Reading','Children & Youth with Exceptionalities','Student Development,Differences,Learning','Reading Instruction','Materials for Teaching Reading','Science Curr,Methods,Matrls,Assessment','Math Curr,Methods,Matrls,Assessment','Theory & Practice in ECE','Soc St Curr,Methods,Matrls,Assessment','Assessment for Reading Instruction','Classroom Organization & Management','Special Education Methods:Elementary','Special Education Methods:Middle School','Intro to the Teaching Seminar/Internship','Assessment Diagnosis & Rx in SpEd','Secondary Reading in Content Area Pt2','Secondary Instructional Assessment','Tech for Literacy,Leadership & Learning','Tech for Literacy,Leadership & Learning','Tech for Literacy,Leadership & Learning','Administration of Student Services','Administration of Student Services','Administration of Student Services','Reading Instruction:Secondary','Reading Diagnosis','Reading Diagnosis/Prescription:Clinical','Current Issues in ECE & Elementary Ed','Topics:Elementary/Middle Physical Sci','Numb,Oper,Alg Thinking E/M School','Found Elem STEM ','Tchg Diverse Learners/Inclusive Setting','Introduction to Educational Research','Introduction to Educational Research','Introduction to Educational Research','	Research-Based Tchng,Lrng,Assessment','Research-Based Tchng,Lrng,Assessment','Research-Based Tchng,Lrng,Assessment','Educational Philosophy in a Diverse Soc','Educational Philosophy in a Diverse Soc','Educational Philosophy in a Diverse Soc','	Princ of Curr Development & Appraisal','Princ of Curr Development & Appraisal','Princ of Curr Development & Appraisal','Principles of Educational Supervision','Principles of Educational Supervision','Principles of Educational Supervision','Teaching Statistics & Probability','Basic Writing Skills','Elements of Compostn ','Elements of Compostn ','Elements of Compostn','Elements of Compostn','Elements of Compostn','Writng about Lit:Humans with Insides','Writng about Lit:Humans with Insides','WrtgLit:Literary Encounters w/Real World','Approaches to Literature','American Literature','Theme:Narratives of Rome & Britain','Theme:Mod Wasteland 20thC English Lit','Thematic St:Arthur:Once & Future King','Genre Studies: The Short Story','Genre Studies: The Woman in the Poem','Genre Studies: Forms in Poetry','Special Topic: Literature and Film','	Shakespeare','Special Topics: Remembering World War I','Literature for Adolescents','Environmental Problems','Intro to Geographic Information Systems','Special Tp:Globalization & the Honey Bee','Pollution Biology','Natural Resource Mgt','Introduction to Playwriting','Pollution Biology','Pollution Biology','Biostatistics','Natural Resource Management','Natural Resource Management','Freshwater Ecology','Freshwater Ecology','French Conversation','German Conversation','Cultural Perspectives on Ger Lit I','Introduction to German LiteratureII','Social Gerontology','Health and Aging','Global Persp/Women, Power & Politics','Dynamics of Leadership','Medieval Europe','History of the United States to 1865','History of United States since 1877','History of United States since 1877','Ancient and Medieval World to 1200','Medieval & Early Modern World, 1200-1800','The Modern World, 1750 to Present','Latin America','Research and Writing in History','Blacks and American Law','Collections: Museums and Archives','Special Tp:Globalization & the Honey Bee','Special Topics: Remembering World War I','Hon Colloq II:Ethics & Epidemics','Honors Colloq II: Plagues and Peoples','Honors Colloq II:Are Humans Unique','Literature of Moral Reflection','Law and Cyberspace','Unraveling the Web','Intermediate Web Development','Computing Hardware/Software Systems','Elements of Computer Programming','Contemporary Issues in Info Tech','Info Assurance & Risk Assessment','Applied Database Systems','Telecommunications and Networking','Management Information Systems','Intro to Data Analytics/Bus Data Mining','Advanced Data Analytics with R','Managing Technical Project Teams','Statistical Methods:Design & Analysis','SpTpc: Leading & Governing Boards','Latin American Lit Popular Culture','Introduction to Law','Fundamental Concepts of Math II','Mathematics of Daily Life','Mathematics of Democracy','Applied Statistics','Applied Statistics','Applied Statistics','Pre-Calculus Mathematics','Pre-Calculus Workshop','Discrete Math','Statistical Concepts and Methods','Modeling and Simulation','Introduction to Abstract Algebra','Explorations in Algebra','Cultures of the Middle East','Prin of Mgmt Intro to Organizations','Prin of Mgmt Intro to Organizations','Principles of Financial Accounting','Principles of Managerial Accounting','Principles of Managerial Accounting','Organizational Theory and Behavior','Principles of Marketing','Personnel Management','Analytical Methods of Management','International Business','Intermediate Accounting II','Auditing','	Investment Analysis','Marketng Research Methods','Marketing Communications Strategy','Marketing Communications Strategy','Cost Accounting','Legal Environment of Business','Foundations of Accounting','Legal Environment of Business','Leadership & Organizational Behavior','Financial Management','Marketing Management','International Management','Organizational Sustainability','Project Management','Project Management', 'Advertising Management','Portfolio and Investment Management','Financial Statement Analysis','Human Resource Management','Strategy & Competitive Advantage','Strategy & Competitive Advantage','SpTpc: Leading & Governing Boards','Fundamentals of Music','Introduction to Music','Introduction to Music','Introduction to Nursing Pharmacology','Adult Health I','Health Assessment','Informatics and Health Care Technology','Contemporary Health Care','Clinical Thanatology','Leadership in Nursing Practice','Contemporary Philosophical Topics','Contemporary Philosophical Topics','Philosophical Issues in Feminism','Ethics','Ethics','Literature of Moral Reflection','General Physics','Introductory Physics II','Mechanics','Thermodynamics & Statistical Mechanics','Chinese Thought','Methods of Political Inquiry','Comparative Politics','9/11 in Global Perspective','Public Policy Analysis','Great Political Trials','Gender and the Law','Introduction to Psychology','Introduction to Psychology','Psychology of Death','Social Psychology','Developmental Psychology','Human Memory','Research Methods II','Research Methods II','Psychology of Aging','Physiological Psychology','Abnormal Psychology','History of Psychology','Behavior Modification','Social Psychology: A Survey','Theory and Principles of Counseling','Diagnosis & Psychopathology','What is"Religion"?Intro to Relig Studies','Principles of Sociology','Principles of Sociology','Sociological Theory','Methods of Social Research','Quantitative Methods for Social Sciences','Social Inequality','Sociology of Sexuality','Child Welfare Policies & Services','Social Policy Human Service Program','Forensic Social Work','Clinical Thanatology','Social Work Methods I','Spanish Conversation','Cultural Perspectives on Spanish Lit II','Spanish Cinema','Principles of Thanatology','Developmental Perspectives:Thanatology','Historical/Multicultural Persp:Thanatol','The Elements of Acting','The Theatre and Films of Buster Keaton', 'Princ & Methods Molecular Genetics', 'Introduction to Bioinformatics', 'Pathogenic Microbiology', 'Princ & Methods Molecular Genetics', 'Introduction to Bioinformatics', 'The Chemical World (CORE-Scientific Thought-Lab)', 'General Chemistry II (CORE-Scientific Thought-Lab)', 'Tests & Measurements', 'Infants & Toddlers:Foundations/Methods', 'Creative Writing', 'Creative Nonfiction', 'Elementary French II (CORE-Foundations/Foreign Language)', 'Intermediate French II (CORE-Foundations/Foreign Language)', 'Elementary German II (CORE-Foundations/Foreign Language)', 'Intermediate German II (CORE-Foundations/Foreign Language)', 'Seminar for Academic Success', 'Algebra Review I', 'Algebra Review II', 'Calculus I (CORE-Computation/Quantitative Literacy)', 'Calculus II', 'Introduction to Tactical Leadership', 'Foundations of Tactical Leadership', 'Leadership and Ethics', 'Officership', 'Beginning Music Theory & Musicianship I (CORE-Art/Visual & Performing)', 'Pediatric Nursing', 'Maternity Nursing', 'First Aid and CPR', 'Stress Assess Contrl (CORE-Foundations/PE/Health & Wellness)', 'Life Wellness and Health (CORE-Foundations/PE/Health & Wellness)', 'Introduction to Exercise Physiology (CORE-Foundations/PE/Health & Wellness)', 'Elementary Statistics (CORE-Computation/Quantitative Literacy)', 'Foundations of Psychological Testing', 'Tests and Measurements', 'Elementary Spanish II (CORE-Foundations/Foreign Language)', 'Intermediate Spanish II', 'Secret Lives of Plants (CORE-Scientific Thought-Lab)', 'Biology of Food & Nutrition (CORE-Scientific Thought-Lab)', 'Newsstand Biology (CORE-Scientific Thought-Lab)', 'This Course Will Bug You (CORE-Scientific Thought-Lab)', 'Evolution and Ecology', 'Intro to Cell Biology & Genetics', 'Anatomy & Physiology for Nurses II', 'Microbiology for Nurses', 'Genetics', 'Microbiology', 'Ornithology', 'Adv Human Anatomy and Physiology', 'Organic Chemistry II', 'Instrumental Methods of Analysis', 'Biological Chemistry Lab Techniques', 'Thermodynamics & Stat Mechanics Lab', 'Child Development', 'Processes & Acquisition of Reading', 'Theory & Practice in ECE', 'Environmental Science Lab (CORE-Scientific Thought-Lab)', 'Intro to Geographic Information Systems', 'Identification of Local Woody Vegetation', 'Introduction to GIS Mapping', 'Introduction to GIS Analysis', 'Adult Health I Lab', 'Health Assessment', 'General Physics (CORE-Scientific Thought-Lab)', 'Introductory Physics II (CORE-Scientific Thought-Lab)', 'Thermodynamics & Stat Mechanics Lab', 'Photojournalism', 'Design (CORE-Art/Visual & Performing)', 'Ceramics I (CORE-Art/Visual & Performing)', 'Digital Photography', 'Drawing II', 'Relief Printmaking I', 'Painting I', 'Ceramic Wheel (CORE-Art/Visual & Performing)', 'Relief Printmaking II', 'SpTpc:Phantasmagoria', 'Drawing III', 'Advanced Printmaking', 'Intermediate Wheel', 'Drawing IV', 'Ceramic Sculpture', 'Ceramic Wheel: Masters Throwing Conc', 'Plates and Platters', 'Brush Making', 'Photographing Ceramics', 'Electric Kilns', 'Wood Firing Theory', 'Clay/Glaze Chemistry Theory & Practice', 'Large Scale and Composite Sculpture', 'Advanced Studies in Ceramic Arts', 'Visual Media Production', 'Graphics', 'Visual Media Production II', 'Graphic Design III', 'Visual Media Production III', 'Seminar: Topics in Art & Archaeology', 'Seminar: Topics in Art History', 'Senior Seminar', 'Seminar in Personal Studio Research', 'Biology Seminar', 'Research Seminar', 'Biomedical Science Seminar', 'Physical Science Literature', 'Seminar in Media Issues', 'Senior Project', 'Seminar', 'Phase III Seminar on Becoming a Teacher', 'Professional Development Seminar', 'Seminar', 'Seminar: Resistances', 'Amazing Archaeological Discoveries (CORE-First Year Seminar)', 'Senior Seminar in Global Studies', 'Honors Sem:Mythology of Death/Afterlife', 'Honors Sem:Breaking the Disney Spell', 'Seminar in Communication Ethics', 'Seminar in Ethics and Leadership', 'Capstone I: Theoretical Framework', 'Research Project in the History of Math (CORE-Global Perspectives)', 'Seminar in Strategic Management', 'Junior Recital', 'Senior Recital', 'Senior Seminar & Practicum', 'Physical Science Literature', 'Phil & Rel Proseminar:Vices & Virtue', 'Internship Colloquium in Political Sci', 'Seminar on Politics', 'Seminar: Introduction to Counseling', 'Seminar in Sociology', 'SoWk Field Seminar', 'Seminar: The Social Work Profession']

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