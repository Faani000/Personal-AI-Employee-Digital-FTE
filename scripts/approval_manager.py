import os
import time
import shutil

PENDING = r"D:\Digital_FTE_Project\AI_Employee_Vault\Pending_Approval"
APPROVED = r"D:\Digital_FTE_Project\AI_Employee_Vault\Approved"
REJECTED = r"D:\Digital_FTE_Project\AI_Employee_Vault\Rejected"

print("Approval Manager Running...")

while True:

    files = os.listdir(PENDING)

    for file in files:

        file_path = PENDING + "\\" + file

        if file.startswith("APPROVED_"):

            shutil.move(file_path,APPROVED+"\\"+file)

            print("Task Approved:",file)

            log_path = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log.txt"

            with open(log_path,"a") as log:

                log.write("Approved: "+file+"\n")

        if file.startswith("REJECTED_"):

            shutil.move(file_path,REJECTED+"\\"+file)

            print("Task Rejected:",file)

            log_path = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log.txt"

            with open(log_path,"a") as log:

                log.write("Rejected: "+file+"\n")

    time.sleep(6)