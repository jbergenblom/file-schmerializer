from collections import defaultdict
import xml.etree.ElementTree as ET
import json
import re
import hashlib

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

def xml_to_json_15_bkp(file_path):
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
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]
        
        return result

    result_dict = xml_to_dict(root)
    
    return result_dict

def xml_to_json_15_2(file_path, record_path="Body.*"):
    tree = ET.parse(file_path)
    root = tree.getroot()
    if record_path:
        # Use record_path to dive down into one specific nested path of the structure and discard the others
        # Sometimes the root tag is just some weird word, like MyTableSomethingName, which is then usually followed by a Body object. Sometimes the following object is called 'response' or something. 
        # But using that dividing tag we should be able to return only the "body" and skip out on objects like headers and other metadata. 
        # How is this done?
        pass
    
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
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    
        
        return result

    result_dict = xml_to_dict(root)
    
    return result_dict

def xml_to_json_15_3(file_path, record_path="Body.*"):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def get_elements_by_path(element, path):
        if not path:
            return [element]
        
        parts = path.split('.', 1)
        current = parts[0]
        remaining = parts[1] if len(parts) > 1 else ''
        
        if current == '*':
            # Get all child elements
            results = []
            for child in element:
                results.extend(get_elements_by_path(child, remaining))
            return results
        else:
            # Find specific element
            results = []
            for child in element:
                if child.tag == current:
                    results.extend(get_elements_by_path(child, remaining))
            return results

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
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    
        
        return result

    if record_path:
        # Get elements at the specified path
        elements = get_elements_by_path(root, record_path)
        if len(elements) == 1:
            return xml_to_dict(elements[0])
        return [xml_to_dict(elem) for elem in elements]
    
    return xml_to_dict(root)

def xml_to_json_15_4(file_path, record_path=None, metadata_path=None):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def get_elements_by_path(element, path):
        if not path:
            return [element]
        
        parts = path.split('.', 1)
        current = parts[0]
        remaining = parts[1] if len(parts) > 1 else ''
        
        if current == '*':
            results = []
            for child in element:
                results.extend(get_elements_by_path(child, remaining))
            return results
        else:
            results = []
            for child in element:
                if child.tag == current:
                    results.extend(get_elements_by_path(child, remaining))
            return results

    def xml_to_dict(element):
        if len(element) == 0:
            return element.text

        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            if child.tag not in result:
                result[child.tag] = child_result
            else:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
        
        if len(result) == 1:
            if isinstance(list(result.values())[0], list):
                return list(result.values())[0]
            else:
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    
        
        return result

    def flatten_dict(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    # Get metadata if path is provided
    metadata = {}
    if metadata_path:
        metadata_elements = get_elements_by_path(root, metadata_path)
        if metadata_elements:
            metadata = xml_to_dict(metadata_elements[0])
            # Flatten metadata to avoid nested structures
            metadata = flatten_dict(metadata)

    # Get main records
    if record_path:
        elements = get_elements_by_path(root, record_path)
        records = []
        
        if len(elements) == 1:
            result = xml_to_dict(elements[0])
            # Handle case where result is a list or needs to be converted to a list
            if not isinstance(result, list):
                if isinstance(result, dict) and any(isinstance(v, list) for v in result.values()):
                    # Extract the list from the dictionary
                    for v in result.values():
                        if isinstance(v, list):
                            result = v
                            break
                else:
                    result = [result]
        else:
            result = [xml_to_dict(elem) for elem in elements]

        # Ensure we have a list of records
        if isinstance(result, list):
            records = result
        else:
            records = [result]

        # Add metadata to each record if it exists
        if metadata:
            for record in records:
                if isinstance(record, dict):
                    record.update(metadata)

        return records
    
    return xml_to_dict(root)

def xml_to_json_15_5(file_path, record_path="Body.*", metadata_path=None, flatten_metadata=True):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def get_elements_by_path(element, path):
        if not path:
            return [element]
        
        parts = path.split('.', 1)
        current = parts[0]
        remaining = parts[1] if len(parts) > 1 else ''
        
        if current == '*':
            results = []
            for child in element:
                results.extend(get_elements_by_path(child, remaining))
            return results
        else:
            results = []
            for child in element:
                if child.tag == current:
                    results.extend(get_elements_by_path(child, remaining))
            return results

    def xml_to_dict(element):
        if len(element) == 0:
            return element.text

        result = {}
        for child in element:
            child_result = xml_to_dict(child)
            if child.tag not in result:
                result[child.tag] = child_result
            else:
                if not isinstance(result[child.tag], list):
                    result[child.tag] = [result[child.tag]]
                result[child.tag].append(child_result)
        
        if len(result) == 1:
            if isinstance(list(result.values())[0], list):
                return list(result.values())[0]
            else:
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    
        
        return result

    def flatten_dict(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    # Get metadata if path is provided
    metadata = {}
    metadata_tag = None
    if metadata_path:
        metadata_elements = get_elements_by_path(root, metadata_path)
        if metadata_elements:
            metadata_tag = metadata_elements[0].tag
            metadata = xml_to_dict(metadata_elements[0])
            if flatten_metadata:
                # Flatten metadata to avoid nested structures
                metadata = flatten_dict(metadata)

    # Get main records
    if record_path:
        elements = get_elements_by_path(root, record_path)
        records = []
        
        if len(elements) == 1:
            result = xml_to_dict(elements[0])
            # Handle case where result is a list or needs to be converted to a list
            if not isinstance(result, list):
                if isinstance(result, dict) and any(isinstance(v, list) for v in result.values()):
                    # Extract the list from the dictionary
                    for v in result.values():
                        if isinstance(v, list):
                            result = v
                            break
                else:
                    result = [result]
        else:
            result = [xml_to_dict(elem) for elem in elements]

        # Ensure we have a list of records
        if isinstance(result, list):
            records = result
        else:
            records = [result]

        # Add metadata to each record if it exists
        if metadata:
            for record in records:
                if isinstance(record, dict):
                    if flatten_metadata:
                        record.update(metadata)
                    else:
                        record[metadata_tag] = metadata

        return records
    
    return xml_to_dict(root)


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

def xml_to_json_18(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    def generate_surrogate_key(element):
        """
        Generate a surrogate key by hashing the string representation 
        of all children's content.
        """
        # Convert element to a hashable string representation
        def element_to_str(el):
            if len(el) == 0:
                return str(el.text or '')
            
            # For elements with children, concatenate their string representations
            return ''.join(element_to_str(child) for child in el)
        
        # Hash the string representation
        hash_input = element_to_str(element)
        return hashlib.md5(hash_input.encode()).hexdigest()
    
    def xml_to_dict(element, parent_key=None):
        # If the element has no children, return its text content
        if len(element) == 0:
            return element.text

        # If the element has children, create a dictionary
        result = {}
        
        # Generate surrogate primary key (XPK)
        result['XPK'] = generate_surrogate_key(element)
        
        # Add foreign key if there's a parent key
        if parent_key:
            result['FK'] = parent_key
        
        # Process children
        child_dict = {}
        for child in element:
            child_result = xml_to_dict(child, result['XPK'])
            
            if child.tag not in child_dict:
                child_dict[child.tag] = child_result
            else:
                # Handle multiple children with the same tag
                if not isinstance(child_dict[child.tag], list):
                    child_dict[child.tag] = [child_dict[child.tag]]
                child_dict[child.tag].append(child_result)
        
        # Merge child dictionary with result
        result.update(child_dict)
        
        # If the dictionary has only one key and that key is a list, return the list
        if len(result) == 1:
            if isinstance(list(result.values())[0], list):
                return list(result.values())[0]
            else:
                k = list(result.keys()).pop()
                if re.search(r'item', k, re.IGNORECASE):
                    return [result[list(result.keys())[0]]]    
        
        return result

    # Convert XML to dictionary with keys
    result_dict = xml_to_dict(root)
    
    return result_dict