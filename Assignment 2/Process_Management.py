# Process Managment Code

# ===============================================
# OS LAB ASSIGNMENT 2
# System Startup, Process Creation & Termination
# Using multiprocessing and logging in Python
# ===============================================

import multiprocessing
import logging
import time
import os

# -----------------------------------------------
# Logging Configuration (Sub-Task 1)
# -----------------------------------------------
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# -----------------------------------------------
# Dummy Process Function (Sub-Task 2)
# Simulates system process execution
# -----------------------------------------------
def system_process(task_name):
    logging.info(f"{task_name} started")
    time.sleep(2)   # Simulating work
    logging.info(f"{task_name} ended")

# -----------------------------------------------
# System Startup Simulation Function
# Creates and manages processes
# -----------------------------------------------
def simulate_system_startup():
    print("\n==============================")
    print("     SYSTEM BOOTING UP...")
    print("==============================")

    # Creating multiple child processes (Sub-Task 3)
    p1 = multiprocessing.Process(target=system_process, args=("Process-1",))
    p2 = multiprocessing.Process(target=system_process, args=("Process-2",))
    p3 = multiprocessing.Process(target=system_process, args=("Background-Service",))

    p1.start()
    p2.start()
    p3.start()

    # Wait for processes to complete (Sub-Task 4)
    p1.join()
    p2.join()
    p3.join()

    print("System Shutdown Completed ✅")
    print("Check process_log.txt for logs.")

# -----------------------------------------------
# Display Log File Content (Optional Feature)
# -----------------------------------------------
def show_logs():
    if not os.path.exists("process_log.txt"):
        print("Log file not generated yet!")
        return

    print("\n======== LOG OUTPUT ========")
    with open("process_log.txt", "r") as f:
        print(f.read())

# -----------------------------------------------
# MAIN MENU
# -----------------------------------------------
if __name__ == "__main__":
    while True:
        print("""
=======================================
SYSTEM PROCESS MANAGEMENT SIMULATOR
=======================================
1. Start System Simulation
2. Show Process Logs
0. Exit
=======================================
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            simulate_system_startup()

        elif choice == "2":
            show_logs()

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

