# Process Managment Code

import os
import subprocess
import time

# ==============================
# Task 1: Basic Process Creation
# ==============================
def task1_process_creation(n):
    print(f"\n--- Task 1: Creating {n} child processes ---")
    for i in range(n):
        pid = os.fork()
        if pid == 0:  # Child
            print(f"Child {i}: PID = {os.getpid()}, Parent PID = {os.getppid()}")
            os._exit(0)

    for _ in range(n):
        os.wait()

# =========================
# Task 2: Execute Commands Using exec()
# =========================
def task2_exec_commands(commands):
    print("\n--- Task 2: Executing commands in child processes ---")
    for cmd in commands:
        pid = os.fork()
        if pid == 0:  # Child
            print(f"Executing command: {' '.join(cmd)}")
            os.execvp(cmd[0], cmd)
            os._exit(0)

    for _ in commands:
        os.wait()

# =========================
# Task 3: Zombie and Orphan Processes
# =========================
def task3_zombie():
    print("\n--- Task 3A: Zombie Process ---")
    pid = os.fork()

    if pid == 0:  # Child
        print("Child running, will finish soon...")
        time.sleep(1)
        print("Child finished")
        os._exit(0)
    else:
        print("Parent NOT calling wait() → Child becomes ZOMBIE for 10 seconds")
        time.sleep(10)


def task3_orphan():
    print("\n--- Task 3B: Orphan Process ---")
    pid = os.fork()

    if pid == 0:  # Child
        print("Child started. Parent will exit immediately.")
        time.sleep(5)
        print(f"Child new parent PID = {os.getppid()}")
        os._exit(0)
    else:
        print("Parent exiting now → child becomes ORPHAN")
        os._exit(0)

# =========================
# Task 4: Read /proc Information
# =========================
def task4_proc_info(pid):
    print(f"\n--- Task 4: Reading /proc/{pid} Information ---")

    try:
        with open(f"/proc/{pid}/status") as f:
            print(f.read())
    except:
        print("Invalid PID or permission denied.")

    try:
        exe_path = os.readlink(f"/proc/{pid}/exe")
        print("Executable Path:", exe_path)
    except:
        print("Could not read executable path.")

    try:
        fds = os.listdir(f"/proc/{pid}/fd")
        print("Open File Descriptors:", fds)
    except:
        print("Could not read file descriptors.")

# =========================
# Task 5: Process Prioritization using nice()
# =========================
def task5_prioritization():
    print("\n--- Task 5: Priority Scheduling Demonstration ---")

    for nice_value in [0, 5, 10]:
        pid = os.fork()
        if pid == 0:  # Child
            os.nice(nice_value)
            print(f"Child PID {os.getpid()} running with nice={nice_value}")
            for _ in range(30_000_000):  # CPU intensive loop
                pass
            print(f"Child with nice={nice_value} finished")
            os._exit(0)

    for _ in range(3):
        os.wait()

# =========================
# MENU FOR EXECUTION
# =========================
if __name__ == "__main__":
    print("""
===============================
PROCESS MANAGEMENT LAB PROGRAM
===============================
Choose a task:
1. Task 1 - Create N Child Processes
2. Task 2 - Execute Commands Using exec()
3. Task 3 - Zombie Process
4. Task 3 - Orphan Process
5. Task 4 - Read /proc Information
6. Task 5 - Process Prioritization
0. Exit
===============================
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of child processes: "))
        task1_process_creation(n)

    elif choice == 2:
        commands = [
            ["ls"],
            ["date"],
            ["ps"]
        ]
        task2_exec_commands(commands)

    elif choice == 3:
        task3_zombie()

    elif choice == 4:
        task3_orphan()

    elif choice == 5:
        pid = input("Enter PID to inspect: ")
        task4_proc_info(pid)

    elif choice == 6:
        task5_prioritization()

    else:
        print("Exiting...")

