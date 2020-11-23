# Generate URL for 10 , true/false questions about computers:
# https://opentdb.com/api.php?amount=10&category=18&type=boolean

# Copy Raw Data and simplify to list of dictionaries
# Replace &quot; with '

question_data = [
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The HTML5 standard was published in 2014.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The common software-programming acronym 'I18N' comes from the term 'Interlocalization'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language 'Python' is based off a modified version of 'JavaScript'.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "MacOS is based on Linux.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "AMD created the first consumer 64-bit processor.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "Early RAM was directly seated onto the motherboard and could not be easily removed.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The NVidia GTX 1080 gets its name because it can only render at a 1920x1080 screen resolution.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first dual-core CPU was the Intel Pentium D.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "medium",
     "question": "The last Windows operating system to be based on the Windows 9x kernel was Windows 98.",
     "correct_answer": "False",
     "incorrect_answers": ["True"]}
]
