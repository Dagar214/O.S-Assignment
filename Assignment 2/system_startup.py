# ==============================================
# OS LAB ASSIGNMENT 2
# System Startup, Process Creation & Termination
# Using multiprocessing and logging in Python
# ==============================================

import multiprocessing
import time
import logging

# ----------------------------------------------
# Sub-Task 1: Initialize Logging Configuration
# ----------------------------------------------
logging.basicConfig(
    filename='process_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(processName)s - %(message)s'
)

# ----------------------------------------------
# Sub-Task 2: Define System Process Function
# ----------------------------------------------
def system_process(task_name):
    """
    Simulates a system process by logging start and end messages
    and waiting 2 seconds to represent work.
    """
    logging.info(f"{task_name} started")
    time.sleep(2)
    logging.info(f"{task_name} ended")

# ----------------------------------------------
# Main Execution (Startup Simulation)
# ----------------------------------------------
if __name__ == '__main__':
    print("====================================")
    print("     SIMULATED SYSTEM STARTUP       ")
    print("====================================")
    print("System Starting...\n")

    # ------------------------------------------
    # Sub-Task 3: Create Processes
    # ------------------------------------------
    p1 = multiprocessing.Process(target=system_process, args=('Process-1',))
    p2 = multiprocessing.Process(target=system_process, args=('Process-2',))
    
    # You can add more processes if needed:
    # p3 = multiprocessing.Process(target=system_process, args=('Process-3',))

    # ------------------------------------------
    # Start Processes
    # ------------------------------------------
    p1.start()
    p2.start()
    # p3.start()

    # ------------------------------------------
    # Sub-Task 4: Wait for Processes to Complete
    # ------------------------------------------
    p1.join()
    p2.join()
    # p3.join()

    print("\nSystem Shutdown.")
    print("Process logs saved in process_log.txt")
