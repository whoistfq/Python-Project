#Imports
import os, re

def message():
    os.system('cls')
    print(
'''
Welcome! <3
-------------------------------------------------------------------------------------------------------------
This Script scrapes the net for CVE numbers exploited by Ransomware Gangs.
Step 1: It grabs the ransomware gang names from https://www.ransom-db.com
Step 2: Make a search to the net, only query results that include the strings "group names" "ransomware" "CVE"
Step 3: For each CVE Number, appends it into a list
Step 4: Gather more information on each CVE number
Step 5: Write the output into a CSV File, with CVE numbers grouped to the name of the Ransomware Gang
Pending:
Step 6: Making use of e.g. pandas, perform data analysis on the data obtained
--------------------------------------------------------------------------------------------------------------

''')
