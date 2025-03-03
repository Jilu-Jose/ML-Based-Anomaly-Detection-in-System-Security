import pandas as pd
import random
import datetime

th_typ = ["Port Scan", "Malware", "Unusual Traffic", "Unusual Traffic", "Unauthorized Access", "Normal Traffic"]
sev_typ = ["Low", "Medium", "High"]
stat = ["Resolved", "Investigating", "Active"]

logs =[]

for i in range(5000):
    timestamp = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
    log_typ = random.choice(th_typ)
    severity = random.choice(sev_typ)
    status = random.choice(stat)

    if log_typ != "Normal Traffic":
        anomaly = 1
    else:
        anomaly = 0
        
    logs.append([timestamp, log_typ, severity, status, anomaly])


log_data = pd.DataFrame(logs, columns=["Timestamp", "Type", "Severity", "Status", "Anomaly"])
log_data.to_csv("system_logs.csv", index = False)

print("Dataset generate: system_logs.csv")



















