import os
import platform
from time import sleep
import requests
import zipfile
import shutil

class c: # define colors and text styles
    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Error          = "\033[31m" + "\033[1m" + "ERROR! " + '\033[0m' + "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Warning = "\033[33m" + "\033[1m" + "WARNING! " + '\033[0m' + "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightError     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"
    Bold         = "\033[1m"
    Underlined   = "\033[4m"
    END          = '\033[0m'

sleepingTime = 0 # debug wait (in seconds) 

def linux():
    # PATHS
    homePath = os.path.expanduser('~') + "/" # path to /home/<user>/
    folderName = ".customcapes" # program's root folder name
    folderPath = homePath + folderName + "/" # path to root folder
    sleep(sleepingTime)

    # ROOT FOLDER CHECK
    if os.path.exists(folderPath): # root folder exists
        print(c.Green + "Root folder: " + folderPath)
    else: # root folder doesn't exist
        print(c.Warning + "Root folder: not found")
        sleep(sleepingTime/2)
        os.mkdir(folderPath) # create root folder
        print(c.Warning + "Created directory: " + folderPath)

    sleep(sleepingTime)

    # CAPES.ZIP DOWNLOAD
    print()
    print(c.Blue + "Downloading capes.zip...")
    downloadURL = "https://skladu.jeme.cz/customcapes/capes.zip" # define url to zip
    response = requests.get(downloadURL) # download zip
    open(folderPath + "capes.zip", "wb").write(response.content) # save zip
    sleep(sleepingTime)
    print(c.Blue + "Capes successfully downloaded!")

    sleep(sleepingTime)

    # CAPES FOLDER CHECK
    print()
    if os.path.exists(folderPath + "capes"): #  capes folder exists
        print(c.Green + "Capes folder: " + folderPath + "capes/")
    else: # capes folder doesn't exist
        print(c.Warning + "Capes folder: not found")
        sleep(sleepingTime/2)
        os.mkdir(folderPath + "capes") # create capes folder
        print(c.Warning + "Created directory: " + folderPath + "capes/")

    sleep(sleepingTime)

    # EXTRACT CAPES.ZIP TO CAPES FOLDER
    print()
    print(c.Cyan + "Extracting capes...")
    with zipfile.ZipFile(folderPath + "capes.zip","r") as zip_ref: # extracting
        zip_ref.extractall(folderPath + "capes")
    sleep(sleepingTime)
    print(c.Cyan + "Capes successfully extracted!")

    sleep(sleepingTime)

    # CAPES SELECTION
    print("\n") # = 2 new lines
    selectedCape = "none"
    availibleCapes = ["custom", "better-light", "birthday", "bug-tracker", "cobalt", "dannybstyle", "migrator", "milionth-sale", "minecon-2011", "minecon-2012", "minecon-2013", "minecon-2015", "minecon-2016", "mojang", "mojang-new", "mojang-old", "prismarine", "ray-cokes", "realms", "scrolls", "translator", "translator-chinese", "translator-japan", "turtle"]
    while selectedCape not in availibleCapes:
        print(c.LightMagenta + "Select an option from the list: " + c.White)
        sleep(sleepingTime/4)
        print(*availibleCapes, sep=", ") # print availibleCapes list
        print()
        sleep(sleepingTime/4)
        selectedCape = input(c.LightMagenta + "Your selection: " + c.LightBlue)
        if selectedCape not in availibleCapes: # input not in availibleCapes list
            print()
            print(c.Error + "\"" + selectedCape + "\" not in the list!")
            sleep(2.5)
            print()
        else: # selection success
            sleep(sleepingTime)
            print()
            if selectedCape == "custom": # when selected custom, ask for path to png file
                customCapePath = input(c.LightMagenta + "Write absolute path to your custom minecraft .png cape: ")
                sleep(sleepingTime)
            print(c.Green + "Selection success!")

    sleep(sleepingTime)

    # MINECRAFT FOLDER PATH
    print()
    minecraftPath = input(c.LightMagenta + "Write absolute path to your .minecraft folder (leave empty for /home/<user>/.minecraft/): ")
    if minecraftPath == "":
        minecraftPath = homePath + ".minecraft/" # when empty, set to default
    
    # CAPE APPLYMENT
    # paths
    print()
    skinsPathOldMC = minecraftPath + "assets/skins/23/" # cape path for old minecraft versions (1.12 and older)
    skinsPathNewMC = minecraftPath + "assets/skins/17/" # cape path for new minecraft versions (1.13 and newer)
    # cape ID constants (I know, it looks awfull...)
    capeIDOldMC = "2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933" # cape ID for old MC versions
    capeIDNewMC = "17f76a23ff4d227a94ea3d5802dccae9f2ae9aa9" # cape ID for new MC versions
    # check if folders exist, if not, create
    if not os.path.exists(skinsPathOldMC): # old MC folder not found, create and add an cape ID file
        print(c.Warning + "23 folder: not found!")
        sleep(sleepingTime/2)
        os.mkdir(skinsPathOldMC)
        addfile = open(skinsPathOldMC + capeIDOldMC, "a").write("") # creates a temporary file to replace with a cape
        print(c.Warning + "Created directory: 23")
        print(c.Warning + "Created file: " + capeIDOldMC)
    else: # old MC folder found
        print(c.Green + "23 folder: exists")
    if not os.path.exists(skinsPathNewMC): # new MC folder not found, create and add an cape ID file
        print(c.Warning + "17 folder: not found!")
        sleep(sleepingTime/2)
        os.mkdir(skinsPathNewMC)
        addfile = open(skinsPathNewMC + capeIDNewMC, "a").write("") # creates a temporary file to replace with a cape
        print(c.Warning + "Created directory: 17")
        print(c.Warning + "Created file: " + capeIDNewMC)
    else: # new MC folder found
        print(c.Green + "17 folder: exists")
    sleep(sleepingTime)
    print()
    print(c.Cyan + "Applying cape...")
    capePath = folderPath + "capes/" + selectedCape + ".png"
    if selectedCape == "custom": # if custom, apply the custom path
        capePath = customCapePath
    # copying
    shutil.copy(capePath, skinsPathOldMC) # copy selected cape to old MC folder
    shutil.copy(capePath, skinsPathNewMC) # copy selected cape to new MC folder
    # removing original MC capes
    os.remove(skinsPathOldMC + capeIDOldMC) # remove old MC original cape
    os.remove(skinsPathNewMC + capeIDNewMC) # remove new MC original cape
    # renaming selected cape's names to IDs
    os.rename(skinsPathOldMC + selectedCape + ".png", skinsPathOldMC + capeIDOldMC) # rename old MC selected cape
    os.rename(skinsPathNewMC + selectedCape + ".png", skinsPathNewMC + capeIDNewMC) # rename new MC selected cape
    sleep(sleepingTime)
    print(c.Cyan + "Cape successfully applied!")
    sleep(sleepingTime)
    print()
    print(c.Green + "Operation success!")


# MAIN
operatingSystem = platform.system() # OS detection

supportedOSs = ["Linux", "Windows"]

if (operatingSystem in supportedOSs): # OS supported
    print()
    print(c.Green + "Running on: " + operatingSystem)
    print()

    if operatingSystem == "Linux":
        linux() # call linux
    elif operatingSystem == "Windows":
        print(c.Error + "Comming Soon!") # windows not supported, comming soon

else: # OS not supported
    print(c.Error + "Unsupported OS system: " + operatingSystem)
    exit()