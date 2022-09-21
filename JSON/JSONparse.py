#!/usr/bin/env python3
import sys
import json
import time
import pyfiglet
from rich import print
# In order to run this file make sure to add executable privileges then run in shell ./JSONparse.py log.json

def srcIPcount(list):        # takes the documented logs into the function
    ip_dict = {}             # creates an empty dictionary
    for ip in list:          # for each ip in the list
        if ip in ip_dict:    # if the IP is in the dictionary
            ip_dict[ip] += 1 # add 1 to value of that IP
        else:                # if the IP isnt in dictionary this will automatically set the key to be that IP
            ip_dict[ip] = 1  # and this will set the value of the key to 1
    max_ip = max(ip_dict.values()) # looks for the most common IP and sets it to max_ip variable
    for key,value in ip_dict.items(): # for each key, value pair in dictionary
        if value == max_ip:  # if the value is the same as the most common IP
            print(f'[red]{"*" * 133}[/red]')
            print(" " * 10, f'[red]{"    ***           "}[/red]', "The occurence of {0} in the adbhoney.json file: {1}".format(key, value), f'[blue]{"                 ***"}[/blue]')
            print(f'[blue]{"*" * 133}[/blue]')
            print()
            time.sleep(4)

def maxDuration(iplist, durlist):
    ipsrc = ''
    duration = ''
    max_dur = 0.00
    IPdurList = []
    durStruct = {key:value for key,value in zip(iplist, durlist)} # merges the key values into a dictionary
    for key,value in durStruct.items():
        fl = float(value)
        if fl > float(max_dur):
            max_dur = value
            duration = value
            ipsrc = key
    print(f'[red]{"*" * 133}[/red]')
    print(" " * 10, f'[red]{"    ***           "}[/red]', "The duration of {0} in the adbhoney.json file: {1}".format(ipsrc, duration), f'[blue]{"           ***"}[/blue]')
    print(f'[blue]{"*" * 133}[/blue]')
    print()
    time.sleep(4)

def main():
    logsList = []
    connList = []
    closList = []
    inputList = []
    durList = []
    file_name = sys.argv[1] 
    file = open(file_name, "r") 
    for line in file:
        
        logDict = json.loads(line)
        logsList.append(logDict)

    for log in logsList:
        if log["eventid"] == "adbhoney.session.connect":
            connList.append(log["src_ip"])
            connList.append(log["dest_ip"])
        if log["eventid"] == "adbhoney.session.closed":
            closList.append(log["src_ip"])
            durList.append(log["duration"])
        if log["eventid"] == "adbhoney.command.input":
            #if log["input"] not in inputList:   # uncomment lines 64 and 65 
                #inputList.append(log["input"])  # then comment out line 66 if you just want unique commands
            inputList.append(log["input"])  

    goodbyer = """


                     $$$$$$\                            $$\                     $$$$$$$\ $$\     $$\ $$$$$$$$\ 
                    $$  __$$\                           $$ |                    $$  __$$\\$$\   $$  |$$  _____|
                    $$ /  \__| $$$$$$\   $$$$$$\   $$$$$$$ |                    $$ |  $$ |\$$\ $$  / $$ |      """
    goodbyew = """                    $$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$ |      $$$$$$\       $$$$$$$\ | \$$$$  /  $$$$$\    """
    goodbyeb = """                    $$ |\_$$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |      \______|      $$  __$$\   \$$  /   $$  __|   
                    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |                    $$ |  $$ |   $$ |    $$ |      
                    \$$$$$$  |\$$$$$$  |\$$$$$$  |\$$$$$$$ |                    $$$$$$$  |   $$ |    $$$$$$$$\ 
                     \______/  \______/  \______/  \_______|                    \_______/    \__|    \________|
                                                                                           
    
    """

    titler = """    


 $$$$$$\  $$\                           $$\ $$$$$$$\             $$\     $$$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ 
$$  __$$\ $$ |                          $$ |$$  __$$\            $$ |    $$  __$$\ $$  __$$\ \_$$  _|\_$$  _|\_$$  _|\_$$  _|\_$$  _|
$$ /  \__|$$ | $$$$$$\  $$\   $$\  $$$$$$$ |$$ |  $$ | $$$$$$\ $$$$$$\   $$ |  $$ |$$ /  $$ |  $$ |    $$ |    $$ |    $$ |    $$ |  """
    titlew = """$$ |      $$ |$$  __$$\ $$ |  $$ |$$  __$$ |$$$$$$$  |$$  __$$\\_$$  _|  $$$$$$$\ |$$ |  $$ |  $$ |    $$ |    $$ |    $$ |    $$ |  """
    titleb ="""$$ |      $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |$$  ____/ $$ /  $$ | $$ |    $$  __$$\ $$ |  $$ |  $$ |    $$ |    $$ |    $$ |    $$ |  
$$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ | $$ |$$\ $$ |  $$ |$$ |  $$ |  $$ |    $$ |    $$ |    $$ |    $$ |  
\$$$$$$  |$$ |\$$$$$$  |\$$$$$$  |\$$$$$$$ |$$ |      \$$$$$$  | \$$$$  |$$$$$$$  | $$$$$$  |$$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ $$$$$$\ 
 \______/ \__| \______/  \______/  \_______|\__|       \______/   \____/ \_______/  \______/ \______|\______|\______|\______|\______|


    """
    print()
    print(f'[red]{"*" * 133}[/red]')
    print(f'[red]{titler}[/red]')
    print(titlew)
    print(f'[blue]{titleb}[/blue]')
    print(f'[blue]{"*" * 133}[/blue]')
    print()

    while True:
        print(" " * 30, "What would you like to know about this json file? (1-4)")
        print()            
        print(" " * 33, "1. Most common IP address to access the server?")
        print()
        print(" " * 33, "2. Longest connected session?")
        print()
        print(" " * 33, "3. List of commands used?")
        print()
        print(" " * 33, "4. Exit")
        user_choice = input()
        if user_choice == '1':
            srcIPcount(connList)
        elif user_choice == '2':
            maxDuration(closList, durList)
        elif user_choice == '3':
            print(f'[red]{"*" * 133}[/red]')
            print(" " * 10, f'[red]{"    ***               "}[/red]', "The List of commands used are as follows:", f'[blue]{"                ***"}[/blue]')
            print()
            time.sleep(1)
            print()
            for cmd in inputList:
                print(f'[red]{"*** "}[/red]', cmd , f'[blue]{"***"}[/blue]')
                print()
                time.sleep(1)
            print(f'[blue]{"*" * 133}[/blue]')
            print()
        elif user_choice == '4':
            print()
            print(f'[red]{"*" * 133}[/red]')
            print(f'[red]{goodbyer}[/red]')
            print(goodbyew)
            print(f'[blue]{goodbyeb}[/blue]')
            print(f'[blue]{"*" * 133}[/blue]')
            print()
            return False
        else:
            print(f'[red]{"*" * 133}[/red]')
            print(" " * 10, f'[red]{"***                        "}[/red]', "Please enter either 1, 2, 3, or 4.", f'[blue]{"                           ***"}[/blue]')
            print(f'[blue]{"*" * 133}[/blue]')
            print()
            time.sleep(3)

if __name__ == "__main__":
    main()