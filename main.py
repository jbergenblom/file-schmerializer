from xml_to_json import xml_to_json_15 as xml_to_json
import json

sources = {
    "hri031": {
        "file": "./samples/HRI031_2024-10-28.xml",
        "path": "CompoundEmployee.person"
    },
    "hri047b": {
        "file": "./samples/HRI047b_AnniessonAB.xml",
        "path": "Transactions"
    },
    "bii333": {
        "file": "./samples/BII333-ID_5f36d0d8.xml",
        "path": "Body.POSTList.POSTItem",
        "header": "HEAD"
    },
    "bii334": {
        "file": "./samples/BII334-ID_2ef92a96.xml",
        "path": "Body.POSTList.POSTItem",
        "header": "HEAD"
    },
    "bii340": {
        "file": "./samples/BII340-575a2dcc.xml",
        "path": "result"
    },
    "bii346": {
        "file": "./samples/BII346-ID_5f36d0d8.xml",
        "path": "DegreeOfFilling.Entry"
    },
    "hri023b-1": {
        "file": "./samples/HRI023b-f3660b51.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item"
    },
    "hri023b-2": {
        "file": "./samples/HRI023b-f3660b51-2.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item"
    },
    "hri023b-3": {
        "file": "./samples/HRI023b-f3660b51-3.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item"
    },
    "hri023b-4": {
        "file": "./samples/HRI023b-f3660b51-4.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item"
    },
    "hri023b-5": {
        "file": "./samples/HRI023b-f3660b51-5.xml",
        "path": "Body.wsdlGetPayrollV2Response.return.item",
        "header": "HEADER"
    }
}

def get_object_under_path(obj, path):
    dotted_path = path.split(".")
    current = obj
    for piece in dotted_path:
        current = current.get(piece)
    return current

if __name__ == "__main__":
    src = sources.get("hri031")
    data = xml_to_json(src.get("file"))
    print(f"data: {json.dumps(data, indent=4)}")
    # records = get_object_under_path(data, src.get("path"))
    # print(f"data: {json.dumps(records, indent=4)}")