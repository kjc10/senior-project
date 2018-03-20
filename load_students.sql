# empty the table
DELETE FROM student;

# load new records into it
LOAD DATA LOCAL INFILE 'student.csv' INTO TABLE student FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '' LINES TERMINATED BY '\n' (student_ID,student_PID,student_last_name,student_first_name,student_middle_name,student_street,student_city,student_state,student_zip,student_email,student_birthdate,student_phone,student_gender_male,student_username,student_grad,student_major,student_class,student_matric,student_credit,student_athlete,student_visa,student_advisor_name,student_advisor_email);
