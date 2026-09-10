def study_agent(task):
    print("Student Task:", task)

    if "exam" in task.lower():
        print("Decision: Create an exam preparation plan.")
    elif "topic" in task.lower():
        print("Decision: Break the topic into smaller study tasks.")
    else:
        print("Decision: Ask for more details about the study goal.")