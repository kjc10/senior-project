drop table if exists view_notes;
drop table if exists notes;
drop table if exists courses;
drop table if exists student;

CREATE TABLE student (
  student_ID int(11) UNIQUE NOT NULL,
  student_PID varchar(11) UNIQUE NOT NULL,
  student_last_name varchar(50) NOT NULL,
  student_first_name varchar(50) NOT NULL,
  student_middle_name varchar(50),
  student_street varchar(100),
  student_city varchar(100),
  student_state varchar(11),
  student_zip varchar(11),
  student_email varchar(50) UNIQUE NOT NULL,
  student_birthdate varchar(50),
  student_phone varchar(45),
  student_gender_male varchar(5),
  student_username varchar(45) UNIQUE,
  student_grad varchar(45) NOT NULL,
  student_major varchar(45),
  student_class varchar(45),
  student_matric varchar(45),
  student_credit varchar(11),
  student_athlete varchar(11),
  student_visa varchar(50),
  student_advisor_name varchar(50),
  student_advisor_email varchar(50),
  role varchar(50) DEFAULT NULL,
  PRIMARY KEY (student_PID)
);

CREATE TABLE courses (
  student_PID varchar(11),
  course_subject varchar(75) UNIQUE,
  course_title varchar(50) NOT NULL,
  course_term varchar(50) NOT NULL,
  instructor_PID varchar(11) NOT NULL,
  instructor_first_name varchar(50) NOT NULL,
  instructor_last_name varchar(50) NOT NULL,
  instructor_email varchar(50) NOT NULL,
  instructor_username varchar(50) NOT NULL,
  course_grade varchar(45),
  course_student_ID int(11),
  PRIMARY KEY (student_PID, course_subject),
  FOREIGN KEY (course_student_ID) references student(student_ID)
    ON DELETE cascade
    ON UPDATE cascade
);

CREATE TABLE notes(
  stud_PID varchar(11),
  notes_course_subject varchar(75),
  notes_title varchar(100),
  notes_path text,
  class_date DATE,
  submission_date DATE,
  comment text,
  PRIMARY KEY (notes_course_subject, notes_title),
  FOREIGN KEY (stud_PID) references student(student_PID)
    ON DELETE cascade
    ON UPDATE cascade,
  FOREIGN KEY (notes_course_subject) references courses(course_subject)
    ON DELETE cascade
    ON UPDATE cascade
);

CREATE TABLE view_notes(
  stud_PID varchar(11),
  course_subj varchar(75),
  PRIMARY KEY (stud_PID, course_subj),
  FOREIGN KEY (stud_PID) references student(student_PID)
    ON DELETE cascade
    ON UPDATE cascade,
  FOREIGN KEY (course_subj) references courses(course_subject)
    ON DELETE cascade
    ON UPDATE cascade
);
