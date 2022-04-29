import clipboard
import sys
import json
import os
import time

def open_file():
    global r_
    global i
    i = 1
    r_ = {}
    try:
        with open("saved.json", 'r') as f:
            r = f.read()
            try:
                r_ = json.loads(r)
            except json.decoder.JSONDecodeError:
                print("[N] File exists but no JSON structure found")

        for key in r_:
            i += 1

    except FileNotFoundError:
        print("File does not exist!")
        print("Creating new file... (saved.json)")

def save():

    open_file()

    x = clipboard.paste()
    try:
        if r_[str(i - 1)] == x:
            print("Duplicate Detected... not writing")
            return
    except KeyError:
        pass

    r_.update({str(i): str(x)})
    with open("saved.json", "w") as f:
        f.write(json.dumps(r_, indent=4))

        

def load():
    open_file() 
    if r_.get('1') == None:
        print("[N] No keys nor values found!")
        time.sleep(1)
        return
    print("What do you want to load?")
    show_keys()
    choice = input()
    try: 
        clipboard.copy(r_.get(choice))
        print(f"Loaded: {r_.get(choice)}")
    except:
        print("Please choose a valid option...")

def delete():
    global r__
    r__ = {}
    open_file() 
    if r_.get('1') == None:
        print("[N] No keys nor values found!")
        time.sleep(1)
        return
    print("Which one is to delete?")
    show_keys()
    choice = input()
    
    r_.pop(choice)
    i = 1
    for key, value in r_.items():
        r__.update({i: value})
        i += 1
    with open("saved.json", 'w') as f:
        f.write(json.dumps(r__, indent=4))
    
    # print("Please use valid option...")


def show_keys():
    i = 1
    for key in r_:
        print(f"[{i}] {r_.get(key)}")
        i += 1

def clear():
    print("Are you sure? (Y/n)")
    while True:
        choice = input().lower()
        if choice == '':
            choice = 'y'
        if choice == 'y':
            with open("saved.json", 'w') as f:
                f.write('')
            print("[N] saved.json has been cleared!")
            break
        elif choice == 'n':
            print("Aborting...")
            break
        else:
            print("Please use (Y/n).")
    
    return


def pr_about():
    cls()
    print("(C) 2022 Luca Zimmermann")
    print("""
  _                      _        
 | |                    (_)       
 | |_ __  __ _ __  __ _  _  _ __  
 | __|\ \/ /| '__|/ _` || || '_ \ 
 | |_  >  < | |  | (_| || || | | |
  \__|/_/\_\|_|   \__,_||_||_| |_|
                                  
                                  
    """)
    print("'txrain' ~ A fully functional Multi-Clipboard Manager")
    input()

cls = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

opt = { 
    '1': "Load",
    '2': "Save",
    '3': "Delete",
    '4': "Clear",
    '5': "Exit",
    '6': "About"
}
choice = ''

def main():
    while True:
        print("What do you want to do?")
        for i in opt:
            print(f"[{i}] {opt[i]}")

        choice = input()
        ogc = opt.get(choice)

        if ogc == "Save":
            save()
        elif ogc == "Load":
            load()
        elif ogc == "Delete":
            delete()
        elif ogc == "Clear":
            clear()
        elif ogc == "Exit":
            exit()
        elif ogc == "About":
            pr_about()

        time.sleep(1)
        cls()

if __name__ == '__main__':
    cls()
    main()
