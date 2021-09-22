import os


def handleGetListRunning():
    output = os.popen('wmic process get description, processid').read()
    print(output)
