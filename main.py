from xml_to_json import xml_to_json_15_5 as xml_to_json
import json

sources = {
    "hri031-28": {
        "file": "./samples/HRI031_2024-10-28.xml",
        "path": "CompoundEmployee.person",
        "path2": None
    },
    "hri031-27": {
        "file": "./samples/HRI031_2024-10-27.xml",
        "path": "CompoundEmployee.person",
        "path2": None
    },
    "hri031-26": {
        "file": "./samples/HRI031_2024-10-26.xml",
        "path": "CompoundEmployee.person",
        "path2": None
    },
    "hri031-25": {
        "file": "./samples/HRI031_2024-10-25.xml",
        "path": "CompoundEmployee.person",
        "path2": None
    },
    "hri031-24": {
        "file": "./samples/HRI031_2024-10-24.xml",
        "path": "CompoundEmployee.person",
        "path2": None
    },
    "hri047b": {
        "file": "./samples/HRI047b_AnniessonAB.xml",
        "path": "Transactions",
        "path2": None
    },
    "bii333": {
        "file": "./samples/BII333-ID_5f36d0d8.xml",
        "path": "Body.POSTList.POSTItem",
        "header": "HEAD",
        "path2": "Body.*"
    },
    "bii334": {
        "file": "./samples/BII334-ID_2ef92a96.xml",
        "path": "Body.POSTList.POSTItem",
        "header": "HEAD",
        "path2": "Body.*"
    },
    "bii340": {
        "file": "./samples/BII340-575a2dcc.xml",
        "path": "result",
        "path2": None
    },
    "bii346": {
        "file": "./samples/BII346-ID_5f36d0d8.xml",
        "path": "DegreeOfFilling.Entry",
        "path2": None
    },
    "hri023b-1": {
        "file": "./samples/HRI023b-f3660b51.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "path2": None
    },
    "hri023b-2": {
        "file": "./samples/HRI023b-f3660b51-2.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "path2": None
    },
    "hri023b-3": {
        "file": "./samples/HRI023b-f3660b51-3.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "path2": None
    },
    "hri023b-4": {
        "file": "./samples/HRI023b-f3660b51-4.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "path2": None
    },
    "hri023b-5": {
        "file": "./samples/HRI023b-f3660b51-5.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "header": "HEADER",
        "path2": "Body.*"
    },
    "hri023b-6": {
        "file": "./samples/HRI023b-f3660b51-6.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "header": "Metaschmata",
        "path2": "Body.*"
    },
    "soi117": {
        "file": "./samples/SOI117b_2131.xml",
        "header": "Header",
        "path2": "InstoreData.*"
    },
    "soi117-2": {
        "file": "./samples/SOI117b_2131-2.xml",
        "header": "Header",
        "path2": "InstoreData.*"
    }
}

def get_object_under_path(obj, path):
    dotted_path = path.split(".")
    current = obj
    for piece in dotted_path:
        current = current.get(piece)
    return current

if __name__ == "__main__":
    for k, src in sources.items():
        data = xml_to_json(src.get("file"), src.get("path2"), src.get("header"), flatten_metadata=False)
        # if k == "bii346":
        #     print(json.dumps(data, indent=4))
        with open(src.get("file").replace(".xml", ".json"), 'w') as json_file:
            json.dump(data, json_file, indent=4)
    
    
# records = get_object_under_path(data, src.get("path"))
# print(f"data: {json.dumps(records, indent=4)}")