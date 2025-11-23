# Assignment 1
# 🧪 OS Lab Assignment 1  
## Process Management Using Python (os Module)

---

### 📌 Course Details
**Course:** Operating Systems Lab  
**Experiment No.:** 1  
**Topic:** Process Creation & Management  
**Language Used:** Python  
**Platform:** Linux / WSL / Ubuntu Terminal

---

## 📁 Folder Contents
This folder contains:

Assignment1

│

├── process_management.py

├── output.txt

├── report.txt

└── README.md


---

## ✅ Objective
The objective of this assignment is to:

- Understand process creation using `fork()`
- Execute system commands using `exec()`
- Demonstrate zombie and orphan processes
- Read process information from `/proc`
- Understand scheduling effect using `nice()` priority values

---

## ✅ Tasks Implemented

### 🔹 Task 1 – Process Creation
- Creates `N` child processes
- Displays:
  - PID
  - Parent PID

### 🔹 Task 2 – Command Execution
- Executes system commands inside child processes:
  - `ls`
  - `date`
  - `ps`

### 🔹 Task 3 – Zombie & Orphan
- Zombie created by not calling `wait()`
- Orphan created when parent exits early

### 🔹 Task 4 – /proc Information
Reads:
- Process status
- Executable path
- Open file descriptors

### 🔹 Task 5 – Priority Scheduling
- Assigns different `nice()` values
- Observes scheduling order

---
## 🛠️ How to Run the Program

### ✅ Step 1: Open Terminal

### ✅ Step 2: Run the Python script


### ✅ Step 3: Select a Task
You will see a menu:

1.Create N Child Processes
2.Execute Commands
3.Zombie Process
4.Orphan Process
5.Read /proc Information
6.Priority Scheduling
7.Exit

Enter the task number to run.

---
## 📌 Sample Output (Short Preview)

--- Task 1: Creating 3 child processes ---
Child 0: PID = 2412, Parent PID = 2408
Child 1: PID = 2413, Parent PID = 2408
Child 2: PID = 2414, Parent PID = 2408


More detailed output is available in:
✅ `output.txt`

---

## ✅ Learning Outcomes
After completing this assignment, we learned:

- Process lifecycle in Linux
- Parent-child relationships
- Zombie and orphan behavior
- Reading `/proc` filesystem
- Effect of scheduling priority

---

## 📝 Files Description

| File | Description |
|------|-------------|
| `process_management.py` | Main program |
| `output.txt` | Sample output for all tasks |
| `report.txt` | Report summary |
| `README.md` | Instructions & documentation |

---

## ✅ Requirements
- Linux Environment / WSL / Ubuntu
- Python 3.x
- Access to `/proc` filesystem
---

## 🚀 Conclusion
This assignment successfully demonstrates process handling concepts in Operating Systems using Python. It provides practical understanding of how Linux manages processes and scheduling.

---

### ✅ Author
**Student Name:** Dev  
**Roll No:** 2301730073  
**University:** K.R. Mangalam University

---



