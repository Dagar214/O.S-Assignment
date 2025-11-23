# 🧪 OS Lab Assignment 2  
## System Startup & Process Management Simulation (multiprocessing + logging)

---

### Course Details
**Course:** B.Tech. C.S.E(Ai & Ml)  
**Subject:** Operating Systems Lab  
**Experiment No.:** 2  
**Topic:** System Startup, Process Creation & Termination Simulation  
**Language Used:** Python  
**Platform:** Linux / WSL / Ubuntu Terminal

---

## Folder Contents

Assignment2

│

├── Process_Management.py

├── output.txt

├── report.txt

└── README.md


---

## ✅ Objective
The objective of this assignment is to:

- Simulate an operating system startup
- Create and execute multiple processes
- Log process activity using `logging`
- Demonstrate process lifecycle:
  - start
  - execution
  - termination
- Generate a system-like log file

---

## ✅ Tasks Implemented

###  Sub-Task 1 – Logging Setup
- Initialized logging with:
  - timestamps
  - process names
  - messages
- Output stored in `process_log.txt`

###  Sub-Task 2 – Process Function
- Created a dummy system process
- Simulated execution using `time.sleep()`

###  Sub-Task 3 – Process Creation
- Created 3 concurrent processes:
  - Process-1
  - Process-2
  - Background-Service

###  Sub-Task 4 – Termination
- Used `join()` to ensure proper shutdown
- Displayed completion message

---

##  How to Run the Program

### ✅ Step 1: Open Terminal


### ✅ Step 2: Run the Python script


### ✅ Step 3: Choose an Option
You will see:

1.Start System Simulation

2.Show Process Logs

3.Exit


Enter the number to execute a task.

---

##  Sample Output Preview

SYSTEM BOOTING UP...

System Shutdown Completed ✅
Check process_log.txt for logs.


More detailed output available in:
✅ `output.txt`

---

##  Log File Preview (process_log.txt)

2025-07-16  - Process-1 - Process-1 started

2025-07-16  - Process-2 - Process-2 started

2025-07-16  - Background-Service - Background-Service started


---

## ✅ Learning Outcomes
After completing this assignment, we learned:

- System startup simulation
- Multiprocessing in Python
- Concurrent process execution
- Logging for monitoring processes
- Proper process shutdown

---

##  Files Description

| File | Description |
|------|-------------|
| `Process_Management.py` | Main program |
| `output.txt` | Sample program output |
| `report.txt` | Implementation report |
| `README.md` | Instructions & documentation |

---

## ✅ Requirements
- Linux Environment / WSL / Ubuntu
- Python 3.x
- multiprocessing module
- logging module

---

##  Conclusion
This assignment successfully demonstrates system-like behavior using Python multiprocessing. The simulation helps understand how an operating system initializes, runs, monitors, and terminates processes.

---

### ✅ Author
**Student Name:** Dev  
**Roll No:** 2301730073

**University:** K.R. Mangalam University

---

