import os
import platform
from time import sleep
import requests
import zipfile
import shutil
import PIL.Image
import signal

class c:  # define colors and text styles
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Error = "\033[31m" + "\033[1m" + "ERROR! " + '\033[0m' + "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Warning = "\033[33m" + "\033[1m" + "WARNING! " + '\033[0m' + "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"
    Bold = "\033[1m"
    Underlined = "\033[4m"
    END = '\033[0m'

def error(text, sleepTime):
    print(c.Error + text)
    sleep(sleepTime)

def warning(text):
    print(c.Warning + text)

errorSleep = 2 # wait after error (in seconds)

def ctrlc_handler(sig, frame): # ctrl + c detection
    print()
    error("KeyboardInterrupt!", 0)
    print(c.LightBlue + "Goodbye :)" + c.Default)
    exit()

signal.signal(signal.SIGINT, ctrlc_handler)

def paths(OS):
    # PATHS
    folderName = ".customcapes"  # program's root folder name
    if OS == "Linux":
        homePath = os.path.expanduser('~') + "/"  # path to /home/<user>/
        rootFolderPath = homePath + folderName + "/"  # path to root folder
    elif OS == "Windows":
        homePath = os.path.expanduser('~') + "\\"  # path to C:\Users\<user>
        rootFolderPath = homePath + folderName + "\\"  # path to root folder
    
    return rootFolderPath, homePath

def checkForRootFolder(rootFolderPath):
    # ROOT FOLDER CHECK
    if os.path.exists(rootFolderPath):  # root folder exists
        print(c.Green + "Root folder: " + rootFolderPath)
    else:  # root folder doesn't exist
        warning("Root folder: not found")
        os.mkdir(rootFolderPath)  # create root folder
        warning("Created directory: " + rootFolderPath)

def downloadCapes(rootFolderPath):
    # CAPES.ZIP DOWNLOAD
    print()
    print(c.Blue + "Downloading capes.zip...")
    downloadURL = "https://skladu.jeme.cz/customcapes/capes.zip"  # define url to zip
    response = requests.get(downloadURL)  # download zip
    open(rootFolderPath + "capes.zip", "wb").write(response.content)  # save zip
    print(c.Blue + "Capes successfully downloaded!")

def checkCapesFolder(rootFolderPath, OS):
    # CAPES FOLDER CHECK
    print()
    if OS == "Linux":
        if os.path.exists(rootFolderPath + "capes"):  # capes folder exists
            print(c.Green + "Capes folder: " + rootFolderPath + "capes/")
        else:  # capes folder doesn't exist
            warning("Capes folder: not found")
            os.mkdir(rootFolderPath + "capes")  # create capes folder
            warning("Created directory: " + rootFolderPath + "capes/")
    elif OS == "Windows":
        if os.path.exists(rootFolderPath + "capes"):  # capes folder exists
            print(c.Green + "Capes folder: " + rootFolderPath + "capes\\")
        else:  # capes folder doesn't exist
            warning("Capes folder: not found")
            os.mkdir(rootFolderPath + "capes")  # create capes folder
            warning("Created directory: " + rootFolderPath + "capes\\")

def extractCapes(rootFolderPath):
    # EXTRACT CAPES.ZIP TO CAPES FOLDER
    print()
    print(c.Cyan + "Extracting capes...")
    with zipfile.ZipFile(rootFolderPath + "capes.zip", "r") as zip_ref:  # extracting
        zip_ref.extractall(rootFolderPath + "capes")
    print(c.Cyan + "Capes successfully extracted!")

def capesSelection():
    # CAPES SELECTION
    print("\n")  # = 2 new lines
    selectedCape = "none"
    availibleCapes = ["CUSTOM", "better-light", "birthday", "bug-tracker", "cobalt", "dannybstyle", "migrator", "milionth-sale", "minecon-2011", "minecon-2012", "minecon-2013",
                      "minecon-2015", "minecon-2016", "mojang", "mojang-new", "mojang-old", "prismarine", "ray-cokes", "realms", "scrolls", "translator", "translator-chinese", "translator-japan", "turtle"]
    while selectedCape not in availibleCapes:
        print(c.LightMagenta + "Select an option from the list: " + c.White)
        print(*availibleCapes, sep=", ")  # print availibleCapes list
        print()
        selectedCape = input(c.LightMagenta + "Your selection: " + c.LightBlue)
        if selectedCape not in availibleCapes:  # input not in availibleCapes list
            print()
            error("\"" + selectedCape + "\" not in the list!", errorSleep)
            print()
        else:  # selection success
            if selectedCape == "custom":  # when selected custom, ask for path to png file
                customCapeFileName = "none"
                customCapeFileHeight = 0
                customCapeFileWidth = 0
                valid = False
                while valid == False: # repeat until valid
                    customCapeFilePath = input(c.LightMagenta + "Write absolute path to your custom minecraft .png cape: " + c.LightBlue)
                    if not customCapeFilePath.endswith(".png"): # check if it's png
                        error("This is not a png file!", 0)
                    elif not os.path.exists(customCapeFilePath): # check if it exists
                        error("This file doesn't exist!", 0)
                    else: # file exists and it's png
                        customCapeFileName = os.path.basename(customCapeFilePath)
                        customCapeFileImage = PIL.Image.open(customCapeFilePath)
                        customCapeFileWidth, customCapeFileHeight = customCapeFileImage.size
                        if not customCapeFileHeight/customCapeFileWidth == 0.5: # check aspect ratio
                            error("Bad aspect ratio! Please use 2:1!", 0)
                        else:
                            valid = True # everithing looks alright
                    if valid == False: # if an error appeared, wait
                        sleep(errorSleep)
            print()
            print(c.Green + "Selection success!")
    if selectedCape == "custom":        
        return selectedCape, customCapeFileName, customCapeFilePath
    else:
        return selectedCape, "none", "none"

def askForMinecraftPath(homePath, OS):
    # MINECRAFT FOLDER PATH
    valid = False
    while not valid:
        print()
        if OS == "Linux":
            minecraftPath = input(
            c.LightMagenta + "Write absolute path to your .minecraft folder (leave empty for /home/<user>/.minecraft/): " + c.LightBlue)
            if minecraftPath == "":
                minecraftPath = homePath + ".minecraft/"  # when empty, set to default
        elif OS == "Windows":
            minecraftPath = input(
            c.LightMagenta + "Write absolute path to your .minecraft folder (leave empty for C:\\Users\\<user>\\AppData\\Roaming\\.minecraft\\): " + c.LightBlue)
            if minecraftPath == "":
                minecraftPath = homePath + "AppData\\Roaming\\.minecraft\\"  # when empty, set to default
        if not os.path.exists(minecraftPath):
            print()
            error("This path doesn't exist!", errorSleep)
        elif not os.path.isdir(minecraftPath):
            print()
            error("This path isn't a directory!", errorSleep)
        else:
            valid = True
    return minecraftPath

def applyCape(minecraftPath, rootFolderPath, selectedCape, customCapeFilePath, customCapeFileName, OS):
    # CAPE APPLYMENT
    print()
    # cape ID constants (I know, it looks awfull...)
    capeIDOldMC = "2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933" # cape ID for old MC versions
    capeIDNewMC = "17f76a23ff4d227a94ea3d5802dccae9f2ae9aa9" # cape ID for new MC versions

    if OS == "Linux":
        # cape path for old minecraft versions (1.12 and older)
        skinsPathOldMC = minecraftPath + "assets/skins/23/"
        # cape path for new minecraft versions (1.13 and newer)
        skinsPathNewMC = minecraftPath + "assets/skins/17/"
        # check if folders exist, if not, create
        if not os.path.exists(minecraftPath + "assets/"):     # assets folder not found, create
            warning("Assets folder: not found!")
            os.mkdir(minecraftPath + "assets/")
            warning("Created directory: assets")
        else:
            print(c.Green + "Assets folder: exists")
        if not os.path.exists(minecraftPath + "assets/skins/"):     # skins folder not found, create
            warning("Skins folder: not found!")
            os.mkdir(minecraftPath + "assets/skins/")
            warning("Created directory: skins")
        else:
            print(c.Green + "Skins folder: exists")
    elif OS == "Windows":
        # cape path for old minecraft versions (1.12 and older)
        skinsPathOldMC = minecraftPath + "assets\\skins\\23\\"
        # cape path for new minecraft versions (1.13 and newer)
        skinsPathNewMC = minecraftPath + "assets\\skins\\17\\"
        # check if folders exist, if not, create
        if not os.path.exists(minecraftPath + "assets\\"):     # assets folder not found, create
            warning("Assets folder: not found!")
            os.mkdir(minecraftPath + "assets\\")
            warning("Created directory: assets")
        else:
            print(c.Green + "Assets folder: exists")
        if not os.path.exists(minecraftPath + "assets\\skins\\"):     # skins folder not found, create
            warning("Skins folder: not found!")
            os.mkdir(minecraftPath + "assets\\skins\\")
            warning("Created directory: skins")
        else:
            print(c.Green + "Skins folder: exists")

    if not os.path.exists(skinsPathOldMC):     # old MC folder not found, create and add an cape ID file
        warning("23 folder: not found!")
        os.mkdir(skinsPathOldMC)
        # creates a temporary file to replace with a cape
        addfile = open(skinsPathOldMC + capeIDOldMC, "a").write("")
        warning("Created directory: 23")
        warning("Created file: " + capeIDOldMC)
    else:  # old MC folder found
        print(c.Green + "23 folder: exists")
        # folder 23 exists, but the file doesnt
        if not os.path.exists(skinsPathOldMC + capeIDOldMC):
            # creates a temporary file to replace with a cape
            addfile = open(skinsPathOldMC + capeIDOldMC, "a").write("")
            warning("Created file: " + capeIDOldMC)
    # new MC folder not found, create and add an cape ID file
    if not os.path.exists(skinsPathNewMC):
        warning("17 folder: not found!")
        os.mkdir(skinsPathNewMC)
        # creates a temporary file to replace with a cape
        addfile = open(skinsPathNewMC + capeIDNewMC, "a").write("")
        warning("Created directory: 17")
        warning("Created file: " + capeIDNewMC)
    else:  # new MC folder found
        print(c.Green + "17 folder: exists")
        # folder 17 exists, but the file doesnt
        if not os.path.exists(skinsPathNewMC + capeIDNewMC):
            # creates a temporary file to replace with a cape
            addfile = open(skinsPathNewMC + capeIDNewMC, "a").write("")
            warning("Created file: " + capeIDNewMC)
    print()
    print(c.Cyan + "Applying cape...")

    if OS == "Linux":
        capePath = rootFolderPath + "capes/" + selectedCape + ".png"
    elif OS == "Windows":
        capePath = rootFolderPath + "capes\\" + selectedCape + ".png"

    if selectedCape == "custom":  # if custom, apply the custom path
        capePath = customCapeFilePath
    # copying
    # copy selected cape to old MC folder
    shutil.copy(capePath, skinsPathOldMC)
    # copy selected cape to new MC folder
    shutil.copy(capePath, skinsPathNewMC)
    # removing original MC capes
    os.remove(skinsPathOldMC + capeIDOldMC)  # remove old MC original cape
    os.remove(skinsPathNewMC + capeIDNewMC)  # remove new MC original cape
    # renaming selected cape's names to IDs
    if selectedCape == "custom":
        os.rename(skinsPathOldMC + customCapeFileName,
                skinsPathOldMC + capeIDOldMC)  # rename old MC selected cape
        os.rename(skinsPathNewMC + customCapeFileName,
                skinsPathNewMC + capeIDNewMC)  # rename new MC selected cape
    else:
        os.rename(skinsPathOldMC + selectedCape + ".png",
                skinsPathOldMC + capeIDOldMC)  # rename old MC selected cape
        os.rename(skinsPathNewMC + selectedCape + ".png",
                skinsPathNewMC + capeIDNewMC)  # rename new MC selected cape
    print(c.Cyan + "Cape successfully applied!")
    print()


# MAIN
operatingSystem = platform.system()  # OS detection

if operatingSystem == "Linux" or operatingSystem == "Windows":  # OS supported
    print()
    print(c.Green + "Running on: " + operatingSystem)
    print()

    rootFolderPath, homeFolderPath = paths(operatingSystem) # get root folder and home folder paths
    checkForRootFolder(rootFolderPath) # check if rootfolder exists, else create
    downloadCapes(rootFolderPath) # download capes.zip to root folder
    checkCapesFolder(rootFolderPath, operatingSystem) # check if capes folder exists, else create
    extractCapes(rootFolderPath) # extract capes to capes folder
    selectedCape, customCapeFileName, customCapeFilePath = capesSelection() # run the capes selection + custom image checks
    minecraftPath = askForMinecraftPath(homeFolderPath, operatingSystem)
    applyCape(minecraftPath, rootFolderPath, selectedCape, customCapeFilePath, customCapeFileName, operatingSystem) # cape applyment
    print(c.Green + "Operation success!" + c.Default)

else:  # OS not supported
    error("Unsupported OS system: " + operatingSystem, 0)
    exit()