# empty the table
DELETE FROM courses;

LOAD DATA LOCAL INFILE 'courses.csv' INTO TABLE courses FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '' LINES TERMINATED BY '\n' (student_PID,course_subject,course_title,course_term,instructor_PID,instructor_first_name,instructor_last_name,instructor_email,instructor_username,course_grade);

