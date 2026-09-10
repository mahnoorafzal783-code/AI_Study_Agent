def identify_subject(task):
    task_lower = task.lower()

    subjects = {
        "math": ["math", "mathematics", "algebra", "geometry", "calculus"],
        "physics": ["physics", "force", "motion", "energy", "electricity"],
        "chemistry": ["chemistry", "chemical", "reaction", "atom", "molecule"],
        "biology": ["biology", "cell", "genetics", "human body", "plant"],
        "english": ["english", "grammar", "essay", "vocabulary", "writing"],
        "computer science": ["computer", "programming", "coding", "python", "software"]
    }

    for subject, keywords in subjects.items():
        for keyword in keywords:
            if keyword in task_lower:
                return subject

    return "general"


def study_agent(task):
    subject = identify_subject(task)

    print("\nSubject detected:", subject)
    print("Task understood:", task)

    if subject == "general":
        print("Decision: I need more details to identify the subject.")
    else:
        print("Decision: I will help the student with this subject.")
def get_action(subject):
    actions = {
        "math": "Solve the problem step-by-step and give a practice question.",
        "physics": "Explain the concept, formula, and solve the problem.",
        "chemistry": "Explain the concept and give a suitable example.",
        "biology": "Explain the topic in simple language and give key points.",
        "english": "Correct the problem and provide a simple explanation.",
        "computer science": "Explain the concept and provide a practical example.",
        "general": "Ask the student for the subject and more details."
    }

    return actions.get(subject, actions["general"])
def run_agent(task):
    subject = identify_subject(task)
    action = get_action(subject)

    print("\n--- StudyMate AI Agent ---")
    print("Subject:", subject)
    print("Student Task:", task)
    print("Agent Decision:", action)      
def choose_next_action(subject):
    if subject == "math":
        return "Solve the problem step-by-step and give a similar practice question."
    elif subject == "physics":
        return "Explain the concept, formula, and solve the problem."
    elif subject == "chemistry":
        return "Explain the concept, then give an example and practice question."
    elif subject == "biology":
        return "Explain the topic simply and summarize the key points."
    elif subject == "english":
        return "Explain the mistake and give a corrected example."
    elif subject == "computer science":
        return "Explain the concept and give a practical example."
    else:
        return "Ask for the subject and details of the student's problem."      
def ask_student():
    print("\n--- StudyMate AI ---")
    task = input("What do you need help with? ")

    subject = identify_subject(task)
    action = choose_next_action(subject)

    print("\nSubject detected:", subject)
    print("Agent decision:", action)    
def create_study_plan(subject, topic):
    print("\n--- Study Plan ---")
    print("Subject:", subject)
    print("Topic:", topic)
    print("1. Understand the basic concept")
    print("2. Learn the important points")
    print("3. Solve a practice question")
    print("4. Review the mistakes")
    print("5. Take a short quiz")    
def get_study_response(task):
    subject = identify_subject(task)

    if subject == "math":
        return "I will explain the mathematics problem step-by-step and provide a similar practice question."
    elif subject == "physics":
        return "I will explain the physics concept, relevant formula, and solution."
    elif subject == "chemistry":
        return "I will explain the chemistry concept with an example and practice question."
    elif subject == "biology":
        return "I will explain the biology topic simply and summarize the key points."
    elif subject == "english":
        return "I will explain the English problem and provide a corrected example."
    elif subject == "computer science":
        return "I will explain the computer science concept with a practical example."
    else:
        return "I can help with this study question. Please provide a little more detail."    
    