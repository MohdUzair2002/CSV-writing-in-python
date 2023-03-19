import time
import csv
# f_report = open("hi.csv", 'w')
with  open("hi.csv", 'w') as f:

 for i in range(1000):
    f=csv.writer(f)
    f.writerow([i])
    # time.sleep(0.05)
    # f_report.flush()
    # f_report.rese
                                                         