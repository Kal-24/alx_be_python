def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            message = f"Note: '{task}' has an unspecified priority"

    if time_bound == "yes" and priority in ["high", "medium"]:
        message += " that requires immediate attention today!"
    elif time_bound == "no" and priority == "low":
        message += ". Consider completing it when you have free time."
    elif time_bound == "no" and priority in ["high", "medium"]:
        message += "."
    elif time_bound == "yes" and priority == "low":
        message += " but is time-bound."

    print(message)


if __name__ == "__main__":
    main()
