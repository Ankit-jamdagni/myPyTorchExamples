import logging
import json

# Opening JSON file
f = open('config.json')
data = json.load(f)

# print(data["logFilePath"])

def my_loggers():
    # creating one logger which send data to 2 handlers i.e. console and & file at the same time
    # CREATING: LOGGER -> HANDLER -> FORMATTER ->
    # ADDING/SETTING: SET FORMATTER TO HANDLER -> ADD HANDLER TO LOGGER
    # START LOGGING

    # 1 LOGGER ONLY SETTING ITS LEVELS
    pyTorchLogger = logging.getLogger("PYTORCHLOGGER")
    pyTorchLogger.setLevel(logging.DEBUG)

    # 2 HANDLERS
    pyTorchConsoleHandler = logging.StreamHandler()
    pyTorchFileHandler = logging.FileHandler(filename=data["logFilePath"], mode=data["logWritingMode"])  # to send logs to a file

    # 3 DEFINING FORMATS
    consoleFormatter = logging.Formatter("%(asctime)s, %(name)s, Line Number:%(lineno)d, Function:%(funcName)s, Level"
                                         ":%(levelname)s, MESSAGE:%(message)s")
    fileFormatter = logging.Formatter("%(asctime)s, %(name)s, Line Number:%(lineno)d, Function:%(funcName)s, Level:%("
                                      "levelname)s, MESSAGE:%(message)s")

    # 4 ADD FORMATS TO HANDLERS
    pyTorchConsoleHandler.setFormatter(consoleFormatter)
    pyTorchFileHandler.setFormatter(fileFormatter)

    # 5 ADDING HANDLERS TO LOGGER
    pyTorchLogger.addHandler(pyTorchConsoleHandler)
    pyTorchLogger.addHandler(pyTorchFileHandler)

    return pyTorchLogger
