Develop Rest-API using django-rest-framework for work with courses and students.

Entities:
  Course:
    - name
    - description
    - start_date
    - end_date
  Student:
    - first_name
    - last_name
    - email
  CourseParticipant:
    - course (FK)
    - student (FK)
    - completed: bool

API:
  - [x] list courses (name, start_date, end_date, students_count, participants(please return 10 first participants))
  - [x] assign/unassign students to/from course
  - [x] report in csv format:
    - student full name
    - number of assigned courses to student
    - number of completed courses by student

While creating report API, please make sure that it would be possible to extend list of possible export formats. 

Cover APIs with tests.
