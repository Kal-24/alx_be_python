def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task.")
        case "low":
            if time_bound == "no":
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
            else:
                print(f"Note: '{task}' is a low priority task that requires immediate attention today!")
        case _:
            print(f"Note: '{task}' has an unspecified priority.")

if __name__ == "__main__":
    main()
