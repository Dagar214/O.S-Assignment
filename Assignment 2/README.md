# Process Creation and Management – OS Lab

## Course Details

* **Course Code:** ENCS351 – Operating System
* **Program:** B.Tech CSE (AI & ML)

## Experiment Title

**Process Creation and Management Using Python OS Module**

---

## Files Included

* `process_management.py` – Python script implementing all lab tasks
* `output.txt` – Sample output of each task
* `report.txt` / `report.pdf` – Experiment report
* `README.md` – Instructions to run the program

---

## Requirements

* Linux-based Operating System (Ubuntu recommended)
* Python 3.x

>  Note: This code uses `os.fork()` and `/proc`, which work only on Linux / Unix systems.

---

## How to Run the Program

1. Open terminal in the project directory
2. Run the Python file:

```bash
python3 process_management.py
```

3. Choose a task from the menu:

```
1 – Process Creation
2 – Command Execution using exec()
3 – Zombie Process
4 – Orphan Process
5 – Read /proc Information
6 – Process Priority using nice()
```

---

## Task Overview

### Task 1 – Process Creation

Creates N child processes using `os.fork()` and displays PID and PPID.

### Task 2 – Command Execution

each child executes Linux commands like `ls`, `date`, `ps` using `execvp()`.

### Task 3 – Zombie & Orphan Process

Demonstrates zombie processes (no `wait()`) and orphan processes (parent exits early).

### Task 4 – /proc Inspection

Reads process information such as name, state, memory usage, executable path, and file descriptors.

### Task 5 – Process Priority

Shows CPU scheduling impact using different `nice()` values.

---

## Output

* Outputs are displayed in the terminal
* Sample output is saved in `output.txt`

---

## Conclusion

This experiment provides hands-on understanding of Linux process creation, execution, scheduling, and monitoring through Python.

---

## Author

**Dev Dagar**

---

Upload all files to LMS and provide GitHub repository link as instructed.
