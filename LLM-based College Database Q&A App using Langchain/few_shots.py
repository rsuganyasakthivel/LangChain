few_shots = [
    {
        "Question":"How much money the college management spent in paying salary per year?",
        "SQLQuery":"SELECT SUM(FacultySalary*12) FROM faculty",
        "SQLResult":"Result",
        "Answer":"8760000"
    },
    {
        "Question":"what is the maximum and minimum scores scored by students in perccentage",
        "SQLQuery":"""SELECT MAX(GPA_percentage) AS Max_GPA_Percentage, MIN(GPA_percentage) AS Min_GPA_Percentage
                        FROM (
                            SELECT (StudentGPA / 4.0) * 100 AS GPA_percentage
                            FROM student
                        ) AS GPA_percentages;
                        """,
        "SQLResult":"Result",
        "Answer":"[(100.0, 32.5)]"
    },
    {
        "Question": "How much salary is paid to each professors who are not HOD?",
        "SQLQuery": "SELECT FacultySalary FROM faculty WHERE FacultyTitle NOT LIKE 'Head Of %'",
        "SQLResult": "Result",
        "Answer": "(60000,60000,60000,60000,60000)"
    },
    {
        "Question":"Which HOD gets the lowest salary?",
        "SQLQuery":"""SELECT FacultyName FROM faculty 
                        WHERE FacultySalary = (SELECT MIN(FacultySalary) FROM faculty WHERE FacultyTitle LIKE 'Head Of %')""",
        "SQLResult":"Result",
        "Answer":"Mike Briley"
    },
    {
        "Question":"How many persons are there in the college(teaching and non-teaching staff and students)",
        "SQLQuery":"SELECT COUNT(*) FROM person",
        "SQLResult":"Result",
        "Answer":"23"
    },
    {
    "Question":"Max salary given to teachers who are not HODs",
        "SQLQuery":"SELECT MAX(FacultySalary) FROM faculty WHERE FacultyTitle NOT LIKE 'Head Of %'",
        "SQLResult":"Result",
        "Answer":"60000"
    }
]