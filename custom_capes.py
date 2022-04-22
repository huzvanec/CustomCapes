import os
import platform
from time import sleep
from turtle import down
import requests
import zipfile
import shutil

class c: #define colors
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

sleepingTime = 1

def linux():
    homePath = os.path.expanduser('~') + "/" # path to /home/<user>/
    folderName = ".customcapes" # program root folder name
    folderPath = homePath + folderName + "/"
    sleep(sleepingTime)

    if os.path.exists(folderPath): # root folder exists
        print(c.Green + "Root folder: " + folderPath)
    else:
        print(c.Warning + "Root folder: not found")
        sleep(sleepingTime/2)
        os.mkdir(folderPath) # create root folder
        print(c.Warning + "Created directory: " + folderPath)

    sleep(sleepingTime)
    # download capes.zip
    print()
    print(c.Blue + "Downloading capes.zip...")
    downloadURL = "https://skladu.jeme.cz/customcapes/capes.zip"
    response = requests.get(downloadURL)
    open(folderPath + "capes.zip", "wb").write(response.content)
    sleep(sleepingTime)
    print(c.Blue + "Capes successfully downloaded!")

    sleep(sleepingTime)
    print()
    if os.path.exists(folderPath + "capes"):
        print(c.Green + "Capes folder: exists")
    else:
        os.mkdir(folderPath + "capes")
        print(c.Warning + "Capes folder: not found")
        sleep(sleepingTime/2)
        print(c.Warning + "Created directory: " + folderPath + "capes/")

    sleep(sleepingTime)
    # extracting capes from capes.zip
    print()
    print(c.Cyan + "Extracting capes...")
    with zipfile.ZipFile(folderPath + "capes.zip","r") as zip_ref:
        zip_ref.extractall(folderPath + "capes")
    sleep(sleepingTime)
    print(c.Cyan + "Capes successfully extracted!")

    sleep(sleepingTime)
    # capes selection
    print()
    print()
    selectedCape = "none"
    availibleCapes = ["custom", "better-light", "birthday", "bug-tracker", "cobalt", "dannybstyle", "migrator", "milionth-sale", "minecon-2011", "minecon-2012", "minecon-2013", "minecon-2015", "minecon-2016", "mojang", "mojang-new", "mojang-old", "prismarine", "ray-cokes", "realms", "scrolls", "translator", "translator-chinese", "translator-japan", "turtle"]
    while selectedCape not in availibleCapes:
        print(c.LightMagenta + "Select an option from the list: " + c.White)
        sleep(sleepingTime/4)
        print(*availibleCapes, sep=", ")
        print()
        sleep(sleepingTime/4)
        selectedCape = input(c.LightMagenta + "Your selection: " + c.LightBlue)
        if selectedCape not in availibleCapes:
            print()
            print(c.Error + "\"" + selectedCape + "\" not in the list!")
            sleep(sleepingTime*2.5)
            print()
        else:
            sleep(sleepingTime)
            print()
            if selectedCape == "custom":
                customCapePath = input(c.LightMagenta + "Write absolute path to your custom minecraft .png cape: ")
                sleep(sleepingTime)
            print(c.Green + "Selection success!")

    sleep(sleepingTime)
    print()
    minecraftPath = input(c.LightMagenta + "Write absolute path to your .minecraft folder (leave empty for /home/<user>/.minecraft/): ")
    if minecraftPath == "":
        minecraftPath = homePath + ".minecraft/"
    skinsPath = minecraftPath + "assets/skins/23/"
    print()
    print(c.Cyan + "Applying cape...")
    capePath = folderPath + "capes/" + selectedCape + ".png"
    if selectedCape == "custom":
        capePath = customCapePath
    shutil.copy(capePath, skinsPath)
    capeID = "2340c0e03dd24a11b15a8b33c2a7e9e32abb2051b2481d0ba7defd635ca7a933"
    os.remove(skinsPath + capeID)
    os.rename(skinsPath + selectedCape + ".png", skinsPath + capeID)
    sleep(sleepingTime)
    print(c.Cyan + "Cape successfully applied!")
    sleep(sleepingTime)
    print()
    print(c.Green + "Operation success!")





operatingSystem = platform.system() # OS detection

supportedOSs = ["Linux", "Windows"]

if (operatingSystem in supportedOSs): # OS supported7
    print()
    print(c.Green + "Running on: " + operatingSystem)
    print()

    if operatingSystem == "Linux":
        linux()
    elif operatingSystem == "Windows":
        print(c.Error + "Comming Soon!")

else: # OS not supported
    print(c.Error + "Unsupported system: " + operatingSystem)
    exit()