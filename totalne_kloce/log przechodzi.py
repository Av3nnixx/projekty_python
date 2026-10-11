logs1 = [
    ("INFO", "2026-03-29", "System started"),
    ("ERROR", "2026-03-29", "Disk full"),
    ("WARNING", "2026-03-28", "High memory usage"),
    ("INFO", "2026-03-28", "User login")
]
def process_logs(logs):
    log_errors = []
    counts = {
    "INFO" : 0,
    "ERROR" : 0,
    "WARNING" : 0,
    }
    for i in logs:
        log_type,date,reason  = i[0],i[1],i[2]
        for t,c in counts.items():
            if i[0] == t:
                counts[t] += 1
        if i[0] == "ERROR":
            log_errors.append(i[2])
    print(counts)
    return  log_errors
process_logs(logs1)