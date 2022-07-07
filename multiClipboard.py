# import out modules here
import sys
import clipboard
import json

# variable that has the name o the json file we use to store the clipboard
SAVED_DATA = "clipboard.json"

#two functions to write and read the json file

# create json file for us: function named save_items passing the filepath and data as parameters
# then open a file with open and put filepath in w mode for write
# open it as a variable f then json.dump writes the python dictionary as a json object to the file f
# and create the file for us
# example: save_items("test.json", {"key": "value"})
# how you save data to a json file


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# how to load data
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

# make sure we have 2 command line arguments. The first one being the name of the  python file, the second is the command we wanna run
# grab what that command is then load data from json file.
# If command is equal to save: we ask to enter key then get whats on the clipbopard and saved it in the dictionary
# and to the json file.
# If command is equal to load: we ask for the key then we take whatever the value is and put it into the users clipboard
# otherwise the key doesnt exits.
# If command is equal to list: print the data


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("data saved!")
    elif command == "load":
        key = input("enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard ")
        else:
            print("key does not exist")
    elif command == "list":
        print(data)
    else:
        print("unknown command")
else:
    print("please pass exactly one command.")
