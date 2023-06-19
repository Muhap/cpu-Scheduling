process_id = []
total_waiting_time = 0
total_turnaround_time = 0

def sjf_non_preemptive(arrival_time, burst_time):
    n = len(arrival_time)


    for i in range(n):
        process_id.append(i)

    n = len(arrival_time)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    processed = [False] * n
    total_time = 0
    remaining_processes = n

    while remaining_processes > 0:
        shortest_job_index = -1
        shortest_burst = float('inf')
        for i in range(n):
            if not processed[i] and arrival_time[i] <= total_time and burst_time[i] < shortest_burst:
                shortest_burst = burst_time[i]
                shortest_job_index = i

        if shortest_job_index == -1:
            total_time += 1
            continue

        process_index = process_id[shortest_job_index]
        completion_time[process_index] = total_time + burst_time[shortest_job_index]
        turnaround_time[process_index] = completion_time[process_index] - arrival_time[shortest_job_index]
        waiting_time[process_index] = turnaround_time[process_index] - burst_time[shortest_job_index]
        processed[shortest_job_index] = True
        remaining_processes -= 1
        total_time += burst_time[shortest_job_index]

    # Prepare the output as a list of lists
    output = []
    for i in range(n):
        output.append([process_id[i], completion_time[i], turnaround_time[i], waiting_time[i]])
    for i in range(len(waiting_time)):
        global total_waiting_time , total_turnaround_time
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    global av
    av = [total_waiting_time/ n, total_turnaround_time / n]
    return output

def retrieveAverage():
    return av




