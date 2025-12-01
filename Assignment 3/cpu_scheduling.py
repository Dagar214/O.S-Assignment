# CPU Scheduling Simulation
# Priority Scheduling and Round Robin Scheduling
# OS Lab Assignment 3

# -----------------------------
# PRIORITY SCHEDULING
# -----------------------------
def priority_scheduling():
    print("\n--- Priority Scheduling ---")
    n = int(input("Enter number of processes: "))

    processes = []  # (pid, burst_time, priority)

    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority for P{i+1} (lower number = higher priority): "))
        processes.append((i + 1, bt, pr))

    # sort process based on priority
    processes.sort(key=lambda x: x[2])

    wt = 0
    total_wt = 0
    total_tat = 0

    print("\nPID\tBT\tPriority\tWT\tTAT")

    for pid, bt, pr in processes:
        tat = wt + bt
        print(f"P{pid}\t{bt}\t{pr}\t\t{wt}\t{tat}")
        total_wt += wt
        total_tat += tat
        wt += bt

    print("Average Waiting Time =", total_wt / n)
    print("Average Turnaround Time =", total_tat / n)


# -----------------------------
# ROUND ROBIN SCHEDULING
# -----------------------------
def round_robin():
    print("\n--- Round Robin Scheduling ---")
    n = int(input("Enter number of processes: "))
    bt = []
    rem_bt = []

    for i in range(n):
        burst = int(input(f"Enter Burst Time for P{i+1}: "))
        bt.append(burst)
        rem_bt.append(burst)

    tq = int(input("Enter Time Quantum: "))

    t = 0  # current time
    wt = [0] * n

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False

                if rem_bt[i] > tq:
                    t += tq
                    rem_bt[i] -= tq
                else:
                    t += rem_bt[i]
                    wt[i] = t - bt[i]
                    rem_bt[i] = 0
        if done:
            break

    total_wt = sum(wt)
    tat = [bt[i] + wt[i] for i in range(n)]

    print("\nPID\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{i+1}\t{bt[i]}\t{wt[i]}\t{tat[i]}")

    print("Average Waiting Time =", total_wt / n)
    print("Average Turnaround Time =", sum(tat) / n)


# -----------------------------
# MAIN MENU
# -----------------------------
if __name__ == "__main__":
    print("""
==============================
CPU SCHEDULING SIMULATION
==============================
1. Priority Scheduling
2. Round Robin Scheduling
0. Exit
==============================
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        priority_scheduling()
    elif choice == 2:
        round_robin()
    else:
        print("Exiting Program")
