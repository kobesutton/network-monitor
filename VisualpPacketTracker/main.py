import os
import time
import psutil
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

# Units of memory sizes
size = ['bytes', 'KB', 'MB', 'GB', 'TB']

# Function that returns bytes in a readable format
def getSize(bytes):
    for unit in size:
        if bytes < 1024:
            return f"{bytes:.1f}{unit}"
        bytes /= 1024

# Prints the Data on the Terminal or Console
def printData():
    # Creating an instance of PrettyTable class
    card = PrettyTable()
    card.set_style(DOUBLE_BORDER)
    # Column Names of the table
    card.field_names = ["Received", "Receiving", "Sent", 'Sending']
    # Adding row to the table
    card.add_row([f"{getSize(netStats2.bytes_recv)}", \
    f"{getSize(downloadStat)}/s", f"{getSize(netStats2.bytes_sent)}", \
    f"{getSize(uploadStat)}/s"])
    print(card)

# psutil.net_io_counters() returns network I/O statistics as a namedtuple
netStats1 = psutil.net_io_counters()

# Getting the data of total bytes sent and received
dataSent = netStats1.bytes_sent
dataRecv = netStats1.bytes_recv

# Running a loop to get the data continuously
while True:
    # Delay for one second
    time.sleep(1)

    # Clear the Terminal or Console
    # For Windows: use 'cls'
    # For Linux and Mac, keep it as it is
    os.system('clear')

    # Getting the network i/o stats again to 
    # count the sending and receiving speed
    netStats2 = psutil.net_io_counters()

    # Upload/Sending speed
    uploadStat = netStats2.bytes_sent - dataSent
    # Receiving/Download Speed
    downloadStat = netStats2.bytes_recv - dataRecv

    # Print the Data
    printData()

    # Agian getting the data of total bytes sent and received
    dataSent = netStats2.bytes_sent
    dataRecv = netStats2.bytes_recv