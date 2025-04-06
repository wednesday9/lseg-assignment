import sys
import json
from assignment.dict_parser import DictParser

def main():
    try:
        json_file = sys.argv[1]
        key = sys.argv[2]
        with open(json_file, 'r') as file:
            data = file.read()
            object = json.loads(data)
            parser = DictParser(object)
            print("object =", object)
            print("key =", key)
            print("value = ", parser.get_value_by_key(key))
    except Exception as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    main()
