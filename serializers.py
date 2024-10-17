import dicttoxml
from zeep import Client
from typing import List, Any

def serialize_to_json(data: List[Any]) -> List[dict]:
    return [obj.__dict__ for obj in data]

def serialize_to_xml(data: List[Any]) -> bytes:
    try:
        return dicttoxml.dicttoxml(serialize_to_json(data))
    except Exception as e:
        print(f"Error during XML serialization: {e}")
        return b''

def serialize_to_soap(data: List[Any]) -> Any:
    try:
        client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
        return client.service.ConvertSpeed(serialize_to_json(data))
    except Exception as e:
        print(f"Error during SOAP request: {e}")
        return None

# Example usage
if __name__ == "__main__":
    class ExampleData:
        def __init__(self, name, value):
            self.name = name
            self.value = value

    data = [ExampleData("example1", 123), ExampleData("example2", 456)]

    json_data = serialize_to_json(data)
    print("JSON Data:", json_data)

    xml_data = serialize_to_xml(data)
    print("XML Data:", xml_data)

    soap_data = serialize_to_soap(data)
    print("SOAP Data:", soap_data)