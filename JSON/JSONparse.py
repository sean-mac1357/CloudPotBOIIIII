#!/usr/bin/env python3
import sys
import json
import time
import pyfiglet
# In order to run this file make sure to add executable privileges then run in shell ./JSONparse.py log.json

def srcIPcount(diction): # takes the documented logs into the function
    ip_dict = {} # creates an empty dictionary
    for log in diction: # for each log in the list
        si = log['src_ip'] # sets the item of each log's IP_src to the variable si
        sp = log['src_port']
        if si in ip_dict: # if 'variable si' is in the dictionary
            ip_dict[si] += 1 # add 1 to value part of dict
        else: # if 'variable si' isnt in dictionary this will automatically set the key
            ip_dict[si] = 1 # and this will set the value of the key to 1
    max_si_value = max(ip_dict.values()) # looks for the most common IP
    for key,value in ip_dict.items(): # for each key, value pair in dictionary
        if value == max_si_value: # if the value is the same as the most common IP
            print("*" * 100)
            print("    ***           The Occurence of {0} in the adbhoney.json file: {1}                 ***".format(key, value))
            print("*" * 100)
            print()
            time.sleep(4)


def main():
    file_name = sys.argv[1] # takes log.txt and assigns it to file_name
    file = open(file_name, "r") # opens the file_name and makes it easy to read the data of the file
    
    duration = ''
    ipsrc = ''
    max_dur = 0.00
    conDict = []
    conOrder = ["eventid", "src_ip", "src_port", "dest_ip", "dest_port", "timestamp", "unixtime", "session", "sensor"] # each log will be broken down and assigned to one of these keys
    #closOrder = ["eventid", "src_ip", "duration", "timestamp", "unixtime", "session", "sensor"]
    #inputOrder = ["eventid", "input", "timestamp", "unixtime", "session", "sensor"]
    conList = [] # empty List that will hold all the logs in an structured database
    inputList = []
    for line in file: # goes through each line (log) of the file
        lines = line.split(",") # splits each section of the log knowing everything before a ; is a value of one of the keys
        
        if lines[0] == '{"eventid": "adbhoney.session.connect"': 
            a1 = lines[0].replace('{"eventid": ', '')
            a2 = a1.replace('"', '')
            conDict.append(a2)
            b1 = lines[1].replace('"src_ip": ', '')
            b2 = b1.replace('"', '')
            conDict.append(b2.replace(' ', ''))
            c1 = lines[2].replace('"src_port": ', '')
            c2 = c1.replace('"', '')
            conDict.append(c2.replace(' ', ''))
            d1 = lines[3].replace('"dest_ip": ', '')
            d2 = d1.replace('"', '')
            conDict.append(d2.replace(' ', ''))
            e1 = lines[4].replace('"dest_port": ', '')
            e2 = e1.replace('"', '')
            conDict.append(e2.replace(' ', ''))
            f1 = lines[5].replace('"timestamp": ', '')
            f2 = f1.replace('"', '')
            conDict.append(f2.replace(' ', ''))
            g1 = lines[6].replace('"unixtime": ', '')
            conDict.append(g1.replace(' ', ''))
            #g2 = g1.replace('"', '')
            h1 = lines[7].replace('"session": ', '')
            h2 = h1.replace('"', '')
            conDict.append(h2.replace(' ', ''))
            i1 = lines[8].replace('"sensor": ', '')
            i2 = i1.replace('"', '')
            i3 = i2.replace('}\n', '')
            conDict.append(i3.replace(' ', ''))

        if lines[0] == '{"eventid": "adbhoney.session.closed"':
            bc1 = lines[1].replace('"src_ip": ', '')
            bc2 = bc1.replace('"', '')
            bc3 = bc2.replace(' ', '')
            cd1 = lines[2].replace('"duration": ', '')
            cd2 = cd1.replace('"', '')
            cd3 = cd2.replace(' ', '')
            cd4 = float(cd3)
            if cd4 > max_dur:
                max_dur = cd4
                duration = cd3
                ipsrc = bc3
        if lines[0] == '{"eventid": "adbhoney.command.input"':
            b1 = lines[1].replace('"input": ', '')
            b2 = b1.replace('"', '')
            inputList.append(b2.replace(' ', ''))
        
        conStruct = {key:value for key,value in zip(conOrder, conDict)} # merges the key values into a dictionary
        conList.append(conStruct) # appends the merged key value pairs into the List
    
    while True:
        print()
        print("*" * 100)
        print()
        result = pyfiglet.figlet_format("CloudPotBOIIIII")
        print(result)

        print("""
               What would you like to know about this json file? (1-4)
                    
                    1. Most common IP address to access the server?

                    2. Longest connected session?

                    3. List of commands used?

                    4. Exit
        """)
        user_choice = input()
        if user_choice == '1':
            srcIPcount(conList)
        elif user_choice == '2':
            print("*" * 100)
            print("    ***           The duration of {0} in the adbhoney.json file: {1}           ***".format(ipsrc, duration))
            print("*" * 100)
            time.sleep(4)
        elif user_choice == '3':
            print("*" * 100)
            print("    ***               The List of commands used are as follows:                ***")
            print("*" * 100)
            time.sleep(3)
            print()
            for cmd in inputList:
                print("*** ",cmd, "***")
                print()
                time.sleep(2)
            print("*" * 100)
        elif user_choice == '4':
            return False
        else:
            print("""
                Please enter either 1, 2, 3, or 4.
            """)
      

if __name__ == "__main__":
    main()