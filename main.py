import json
import sys
import xml.etree.ElementTree as ET

def get_target_by_id(id):
    #print("Hello World!", id)
    tree = ET.parse('sma_gentext.xml')
    trans_units = tree.getroot().findall(".//trans-unit")

    for unit in trans_units:
        if unit.attrib['id'] == id:
            unit_text = unit.find(".//target").text
            #print(unit_text)
            return unit_text
    return


def write_to_json_file(id, target_text):
    print("Found 'target' element on id: " + id + ". Writing the value to unit.json")
    dict = {
        "id": id,
        "target": target_text
        }
    
    with open("unit.json", "w") as f:
        json.dump(dict, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error! No argument. Use the script like this: python main.py <ID>")
        exit(0)

    id = sys.argv[1]
        
    target_text = get_target_by_id(id)
    
    if target_text is not None:
        write_to_json_file(id, target_text)
    else:
        print("Id not found in xml file. Try another input.")