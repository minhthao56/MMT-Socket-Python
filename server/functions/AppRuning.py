import psutil
import json
from models.ProcessModel import ProcessModel


def handleGetListRunning():
    listProcess = []
    for process in psutil.process_iter():
        Name = process.name()  # Name of the process
        ID = process.pid  # ID of the process
        objectProcess = ProcessModel(id=ID, name=Name)
        listProcess.append(objectProcess)

    listJOSN = json.dumps([ob.__dict__ for ob in listProcess])
    return listJOSN
