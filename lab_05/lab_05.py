import json

def get_filename():
    return input("Input filename: ")
    

def read_json(json_file):
    print("Start reading...")
    with open(json_file, 'r', encoding='utf-8') as file:
        print("Success.")
        return json.load(file)

def create_light(dictionary):
    pass

def main():
    dict_js = read_json(get_filename())

    
if __name__ == "__main__":
    main()
