from collections import defaultdict
import xml.etree.ElementTree as ET
import json
import re

def xml_to_json(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    for child in root:
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        data.append(record)
    
    return data

def xml_to_json_2(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    for child in root:
        data.append(parse_element(child))
    
    return data

def xml_to_json_3(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    def parse_root(element):
        if len(element) == 0:
            return element.text
        parsed_data = {}
        for child in element:
            if child.tag not in parsed_data:
                parsed_data[child.tag] = []
            parsed_data[child.tag].append(parse_element(child))
        return parsed_data

    data.append(parse_root(root))
    
    return data

def xml_to_json_4(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    def parse_root(element):
        if len(element) == 0:
            return element.text
        parsed_data = {}
        for child in element:
            if child.tag not in parsed_data:
                parsed_data[child.tag] = []
            parsed_data[child.tag].append(parse_element(child))
        return parsed_data

    # Parse the root element and extract all records
    parsed_root = parse_root(root)
    
    # Flatten the structure to get a list of records
    for key, value in parsed_root.items():
        if isinstance(value, list):
            data.extend(value)
    
    return data

def xml_to_json_5(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    def extract_records(element):
        records = []
        for child in element:
            if len(child) > 0:
                records.extend(extract_records(child))
            else:
                records.append({element.tag: parse_element(element)})
                break
        return records

    # Extract all records from the root element
    data = extract_records(root)
    
    return data

def xml_to_json_6(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = {}
        for child in element:
            if len(child) > 0:
                parsed_data[child.tag] = parse_element(child)
            else:
                parsed_data[child.tag] = child.text
        return parsed_data

    def extract_records(element):
        records = []
        for child in element:
            if len(child) > 0:
                records.append(parse_element(child))
        return records

    # Assuming the first level of children under the root are the records
    for child in root:
        data.extend(extract_records(child))
    
    return data

def xml_to_json_7(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = defaultdict(list)
        for child in element:
            if len(child) > 0:
                child_data = parse_element(child)
                if child.tag in parsed_data:
                    if isinstance(parsed_data[child.tag], list):
                        parsed_data[child.tag].append(child_data)
                    else:
                        parsed_data[child.tag] = [parsed_data[child.tag], child_data]
                else:
                    parsed_data[child.tag] = child_data
            else:
                if child.tag in parsed_data:
                    if isinstance(parsed_data[child.tag], list):
                        parsed_data[child.tag].append(child.text)
                    else:
                        parsed_data[child.tag] = [parsed_data[child.tag], child.text]
                else:
                    parsed_data[child.tag] = child.text
        return dict(parsed_data)

    # Extract all records from the root element
    for child in root:
        data.append(parse_element(child))
    
    return data

def xml_to_json_8(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = defaultdict(list)
        for child in element:
            if len(child) > 0:
                child_data = parse_element(child)
                if child.tag in parsed_data:
                    if isinstance(parsed_data[child.tag], list):
                        parsed_data[child.tag].append(child_data)
                    else:
                        parsed_data[child.tag] = [parsed_data[child.tag], child_data]
                else:
                    parsed_data[child.tag] = child_data
            else:
                if child.tag in parsed_data:
                    if isinstance(parsed_data[child.tag], list):
                        parsed_data[child.tag].append(child.text)
                    else:
                        parsed_data[child.tag] = [parsed_data[child.tag], child.text]
                else:
                    parsed_data[child.tag] = child.text
        return dict(parsed_data)

    # Extract all records from the root element
    for child in root:
        data.append(parse_element(child))
    
    return data

def xml_to_json_9(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = defaultdict(list)
        for child in element:
            child_data = parse_element(child) if len(child) > 0 else child.text
            if child.tag in parsed_data:
                if isinstance(parsed_data[child.tag], list):
                    parsed_data[child.tag].append(child_data)
                else:
                    parsed_data[child.tag] = [parsed_data[child.tag], child_data]
            else:
                parsed_data[child.tag] = child_data
        return {k: v if len(v) > 1 else v[0] for k, v in parsed_data.items()}

    # Extract all records from the root element
    for child in root:
        data.append(parse_element(child))
    
    return data

def xml_to_json_10(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = defaultdict(list)
        for child in element:
            child_data = parse_element(child) if len(child) > 0 else child.text
            parsed_data[child.tag].append(child_data)
        # Convert lists with a single item to just the item
        return {k: v if len(v) > 1 else v[0] for k, v in parsed_data.items()}

    def simplify_structure(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    data[key] = [simplify_structure(item) for item in value]
                elif isinstance(value, dict):
                    data[key] = simplify_structure(value)
        return data

    # Extract all records from the root element
    for child in root:
        data.append(simplify_structure(parse_element(child)))
    
    return data

def xml_to_json_11(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    def parse_element(element):
        parsed_data = defaultdict(list)
        for child in element:
            child_data = parse_element(child) if len(child) > 0 else child.text
            parsed_data[child.tag].append(child_data)
        # Convert lists with a single item to just the item
        return {k: v if len(v) > 1 else v[0] for k, v in parsed_data.items()}

    def simplify_structure(data):
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    # If the list contains dictionaries, simplify each dictionary
                    if all(isinstance(item, dict) for item in value):
                        data[key] = [simplify_structure(item) for item in value]
                    # If the list contains only one dictionary, simplify it to a single dictionary
                    elif len(value) == 1 and isinstance(value[0], dict):
                        data[key] = simplify_structure(value[0])
                elif isinstance(value, dict):
                    data[key] = simplify_structure(value)
        return data

    # Extract all records from the root element
    for child in root:
        data.append(simplify_structure(parse_element(child)))
    
    return data

def xml_to_json_12(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    # Assuming the root has only one child which is the main container
    main_container = root[0]
    
    def xml_to_dict(element):
        # If the element has no children, return its text content
        if len(element) == 0:
            return element.text
        
        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            
            # If the tag is already in the result, it means we have a list
            if child.tag in result:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
            else:
                result[child.tag] = child_result
        
        return result

    records = []
    for record in main_container:
        records.append(xml_to_dict(record))
    
    # return json.dumps(records, indent=4)
    return records

def xml_to_dict(element):
    # If the element has no children, return its text content
    if len(element) == 0:
        return element.text

    # If the element has children, create a dictionary
    result = {}
    for child in element:
        child_result = xml_to_dict(child)
        if child.tag not in result:
            result[child.tag] = child_result
        else:
            if not isinstance(result[child.tag], list):
                result[child.tag] = [result[child.tag]]
            result[child.tag].append(child_result)
    
    # If the dictionary has only one key and that key is a list, return the list
    if len(result) == 1 and isinstance(list(result.values())[0], list):
        return list(result.values())[0]
    
    return result

def xml_to_json_13(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def xml_to_dict(element):
        # If the element has no children, return its text content
        if len(element) == 0:
            return element.text

        # If the element has children, create a dictionary
        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            if child.tag not in result:
                result[child.tag] = child_result
            else:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
        
        # If the dictionary has only one key and that key is a list, return the list
        if len(result) == 1 and isinstance(list(result.values())[0], list):
            return list(result.values())[0]
        
        return result

    result_dict = xml_to_dict(root)
    
    return result_dict

def xml_to_json_14(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def xml_to_dict(element):
        # If the element has no children, return its text content
        if len(element) == 0:
            return element.text

        # If the element has children, create a dictionary
        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            if child.tag not in result:
                result[child.tag] = child_result
            else:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
        
        # If the dictionary has only one key and that key is a list, return the list
        if len(result) == 1 and isinstance(list(result.values())[0], list):
            return list(result.values())[0]
        
        # If the dictionary has only one key and that key is not a list, wrap it in a list
        if len(result) == 1 and not isinstance(list(result.values())[0], list):
            return [result]
        
        return result

    result_dict = xml_to_dict(root)
    
    return result_dict

def xml_to_json_15(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def xml_to_dict(element):
        # If the element has no children, return its text content
        if len(element) == 0:
            return element.text

        # If the element has children, create a dictionary
        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            if child.tag not in result:
                result[child.tag] = child_result
            else:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
        
        # If the dictionary has only one key and that key is a list, return the list
        if len(result) == 1:
            if isinstance(list(result.values())[0], list):
                return list(result.values())[0]
            else:
                if re.search(r'item', list(result.keys()).pop(), re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    

        # If the dictionary has only one key and that key is not a list, wrap it in a list
        # if len(result) == 1 and not isinstance(list(result.values())[0], list):
        #     # return [result[list(result.keys())[0]]]
        #     # return result[list(result.keys())[0]]
        #     return result
        
        # Check for elements that should be lists based on their children's name
        # for key in result:
        #     if isinstance(result[key], dict):
        #         for subkey in result[key]:
        #             if re.search(r'item', subkey, re.IGNORECASE):
        #                 result[key] = [result[key]]
        #                 break
        #     elif re.search(r'item', key, re.IGNORECASE):
        #         result[key] = [result[key]]
        
        return result

    result_dict = xml_to_dict(root)
    
    return result_dict

def xml_to_json_16(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def parse_element(element):
        """Parse an XML element recursively into a Python dictionary."""
        # If the element has no children and no attributes, treat it as a scalar value
        if len(element) == 0 and not element.attrib:
            return element.text

        # Initialize the dictionary to store the parsed data
        parsed_data = defaultdict(list)
        
        for child in element:
            # Parse child element recursively
            child_data = parse_element(child)
            # If there's already a key, it's a list of elements; otherwise, treat it as a single value
            if child.tag in parsed_data:
                # If the element is not a list yet, convert to list
                if not isinstance(parsed_data[child.tag], list):
                    parsed_data[child.tag] = [parsed_data[child.tag]]
                parsed_data[child.tag].append(child_data)
            else:
                parsed_data[child.tag] = child_data

        # Flatten the dictionary if there are multiple children of the same tag
        for key, value in parsed_data.items():
            if isinstance(value, list) and len(value) == 1:
                parsed_data[key] = value[0]

        # Return a normal dictionary instead of defaultdict
        return dict(parsed_data)

    # Root element should have multiple children, treat each as a record
    result_dict = [parse_element(child) for child in root]
    
    return result_dict

def xml_to_json_17(file_path):
    def parse_element(element):
        # Function to determine if an XML element should be treated as a list
        def is_list(elements):
            # If multiple elements with the same tag exist, treat them as a list
            if len(elements) == 0:
                return False
            first_tag = elements[0].tag
            return all(el.tag == first_tag for el in elements)

        # If element has no children and only contains text, return the text directly
        if len(element) == 0:
            return element.text.strip() if element.text else None

        # Group child elements by their tags
        children_by_tag = defaultdict(list)
        for child in element:
            children_by_tag[child.tag].append(child)

        # Parse each group of children
        parsed_data = {}
        for tag, children in children_by_tag.items():
            if is_list(children):
                # If the tag should be a list, parse each child and make a list
                parsed_data[tag] = [parse_element(child) for child in children]
            else:
                # If not a list, parse the single child element
                parsed_data[tag] = parse_element(children[0])

        return parsed_data

    # Parse the XML string and get the root element
    # root = ET.fromstring(xml_string)
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Find the main list element (in your example, it's <CompoundEmployee>)
    # Assuming it's the first child of the XML root
    main_list_element = next(iter(root), None)
    if main_list_element is None:
        return []

    # Parse each record in the main list
    parsed_records = [parse_element(record) for record in main_list_element]
    
    # Convert the parsed records to JSON-like data
    return parsed_records