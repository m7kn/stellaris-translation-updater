import re
import yaml


def convert_doublequotes(line: str) -> str:
    """Add backslash to inner doublequotes"""
    converted_str = line
    count_dq = line.count('"')
    if count_dq > 2:
        first_dq_index = line.find("\"")
        last_dq_index = line.find("\"", -1)
        inner_str = line[first_dq_index+1:last_dq_index]
        inner_str = inner_str.replace("\"", "\\\"")
        converted_str = line[:first_dq_index] + inner_str + line[last_dq_index:]

    return converted_str


def convert_line(line: str) -> str:
    """Convert a line to yaml parsing"""
    line = re.sub(r":\d+ ", ": ", line, 1)
    line = re.sub(r"\"\".", "\"", line)
    line = re.sub(r"\.\"\"", ".\"", line, 1)
    line = re.sub(r"\.\\\"", ".\"", line)
    line = convert_doublequotes(line)
    
    return line


def create_data(line: str) -> dict:
    """Create dictionary data from the line string"""
    converted_txt = convert_line(line)
    key = ""
    value = ""
    try:
      dict_data = yaml.safe_load(converted_txt)
    except:
      data = line.split(':', 1)
      key = data[0]
      value = data[1]
      dict_data = None

    if dict_data:
        key = list(dict_data.keys())[0]
        value = dict_data[key]
      
    return {
        "orig_txt": line,
        "converted_txt": converted_txt,
        "key": key,
        "value": value
    }


def find_key(datalist: list, key: str) -> str:
    """Find a key in a datalist"""
    result = None
    for item in datalist:
        item_key = item["key"]
        if item_key:
            if item_key == key:
                result = item
                break

    return result


def get_keys(datalist: list) -> list:
    """Get all datalist keys"""
    keys = []
    for item in datalist:
        key = item["key"]
        if key:
            keys.append(key)

    return keys


def create_datalines(lines_english, lines_translated):
    """Create datalines"""
    datalines_eng = []
    datalines_tr = []
    for line_eng in lines_english:
        datalines_eng.append(create_data(line_eng))
    for line_tr in lines_translated:
        datalines_tr.append(create_data(line_tr))
    
    return (datalines_eng, datalines_tr)
  
  
def find_missing_keys(datalines_eng, datalines_tr):
    """Find missing keys"""
    missing_data = []
    for data_eng in datalines_eng:
        if data_eng:
            data_eng_key = data_eng["key"]
            if data_eng_key and not find_key(datalines_tr, data_eng_key):                
                missing_data.append(data_eng)

    return missing_data
  