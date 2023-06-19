av = []
wt=[]
tat=[]
total_wt= 0.0
total_tat = 0.0

total_wt = float(total_wt)
total_tat = float(total_tat)

top = 0
a_tat = 0.0
a_wt = 0.0
at = []
bt = []
ct = []


def fcfs(at , bt):

    n = len(at)
    global top, a_tat, a_wt
    for i in range(n):
        if i == 0:
            top = top + bt[i]
            ct.append(top)
        elif i > 0:
            if top < at[i]:
                top = at[i] + bt[i]
                ct.append(top)
            else:
                top = top + bt[i]
                ct.append(top)
    print("Completion Time calculated ....")

    for i in range(n):
        var = ct[i] - at[i]
        tat.append(var)
        var = tat[i] - bt[i]
        wt.append(var)
    print("Turn around Time calculated ....")
    print("Waiting Time calculated ....")

    print("PID\t","AT\t","BT\t","CT\t","TAT\t","WT")
    for i in range(n):
        print(str((i+1)), "\t",str(at[i]), "\t",str(bt[i]), "\t",str(ct[i]), "\t",str(tat[i]), "\t",str(wt[i]))
        a_tat = a_tat + tat[i]
        a_wt = a_wt + wt[i]

    a_tat = a_tat/n
    a_wt = a_wt/n
    print("Average Turn around Time = %d"%a_tat)
    print("Average waiting Time = %d"%a_wt)
    global av
    av = [a_wt, a_tat]
    final = [at, bt, wt,tat]
    return final

def retrieveAverage():
    return av


