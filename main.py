"""
main.py

Menu and user interaction for the TB System Resource Monitor.
Run this file to start the program:

    python main.py
"""

import monitor
import logger

def print_menu():
    """
    Print the main menu.
    """

    print()
    print("=" * 32)
    print("    TB System Resource Monitor")
    print("=" * 32)
    print("1. View Current System Status")
    print("2. Start Live Monitor")
    print("3. View Top Processes")
    print("4. Save Current Snapshot")

    # TODO: Print the last two menu options (5 and 6).
    print("5. View System Information")
    print("6. Exit")
    print("=" * 32)


def pause():
    """
    Wait for the user to press Enter before showing the menu again.
    """

    input("\nPress Enter to return to the menu...")

def view_current_status():
    """
    Menu option 1: show the current status and any warnings.
    """

    print("\nGathering system information...")

    # TODO: Get a resource summary from the monitor module.
    summary = monitor.get_resource_summary()

    # TODO: Display the summary, then display any warnings.
    monitor.display_resource_summary(summary)
    print()
    monitor.display_warnings(summary)

def save_current_snapshot():
    """
    Menu option 4: save the current status to the CSV log.
    """

    print("\nGathering system information...")

    summary = monitor.get_resource_summary()

    try:
        # TODO: Save the summary using the logger module.
        file_path = logger.save_snapshot(summary)
        print(f"Snapshot saved to: {file_path}")

    # TODO: Catch the general file error described above.
    except OSError:
        print("Sorry, the snapshot could not be saved.")
        print("Make sure the CSV file is not open in another program.")

def main():
    """
    Run the menu loop until the user chooses Exit.
    """

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_current_status()
            pause()

        # TODO: Option 2 starts the live monitor.
        elif choice == "2":
            monitor.start_live_monitor()
            pause()

        # TODO: Option 3 shows the top processes.
        elif choice == "3":
            monitor.display_top_processes()
            pause()

        # TODO: Option 4 saves a snapshot (use your function from Step 11.4).
        elif choice == "4":
            save_current_snapshot()
            pause()

        # TODO: Option 5 shows the system information.
        elif choice == "5":
            monitor.display_system_info()
            pause()

        # TODO: Option 6 says goodbye and exits the loop.
        elif choice == "6":
            print("Goodbye!")
            break

        # TODO: Anything else is an invalid choice.
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    try:
        # TODO: Call the main() function.
        main()

    # TODO: Catch Ctrl+C (KeyboardInterrupt) and end-of-input (EOFError).
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")