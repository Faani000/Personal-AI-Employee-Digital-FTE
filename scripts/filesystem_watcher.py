import time
import os
import shutil

INBOX = "D:\Digital_FTE_Project\AI_Employee_Vault/Inbox"
NEEDS_ACTION = "D:\Digital_FTE_Project\AI_Employee_Vault/Needs_Action"

print("Watcher Running...")

while True:

    files = os.listdir(INBOX)

    for file in files:

        source = INBOX + "/" + file
        dest = NEEDS_ACTION + "/" + file

        if os.path.isfile(source):

            shutil.move(source,dest)

            print("Moved:",file)

            log_path = r"D:\Digital_FTE_Project\AI_Employee_Vault\Logs\activity_log.txt"

            with open(log_path,"a") as log:

                log.write("Task detected: "+file+"\n")

    time.sleep(5)