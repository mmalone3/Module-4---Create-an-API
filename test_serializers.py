import unittest
from unittest.mock import patch, MagicMock
from serializers import serialize_to_json, serialize_to_xml, serialize_to_soap

class ExampleData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class TestSerializers(unittest.TestCase):
    def setUp(self):
        self.data = [ExampleData("example1", 123), ExampleData("example2", 456)]

    def test_serialize_to_json(self):
        expected_json = [{'name': 'example1', 'value': 123}, {'name': 'example2', 'value': 456}]
        self.assertEqual(serialize_to_json(self.data), expected_json)

    def test_serialize_to_xml(self):
        xml_data = serialize_to_xml(self.data)
        self.assertTrue(xml_data.startswith(b'<?xml'))

    @patch('serializers.Client')
    def test_serialize_to_soap(self, MockClient):
        mock_service = MockClient.return_value.service
        mock_service.ConvertSpeed.return_value = 'mocked response'
        
        soap_data = serialize_to_soap(self.data)
        self.assertEqual(soap_data, 'mocked response')

if __name__ == '__main__':
    unittest.main()