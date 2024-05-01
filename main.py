import json

def generate_master_list(master_list_str, adventure_type):
    master_list_str = append_sub_list(master_list_str, adventure_type, "equipment")
    master_list_str = append_sub_list(master_list_str, adventure_type, "essentials")
    return master_list_str

def append_sub_list(master_list_str, adventure_type, sub_list_name):
    filename = sub_list_name + ".json"
    with open(filename) as json_file:
        full_dict = json.load(json_file)
    sub_list = full_dict[adventure_type]
    # Append sub-list to final_list.
    master_list_str = master_list_str + "\n" + sub_list_name
    for item in sub_list:
        master_list_str = master_list_str + "\n" + "- " + item
    return master_list_str

if __name__ == "__main__":
    print("hello world")
    # Generate master list.
    master_list_str = generate_master_list("", "camping")
    print(master_list_str)