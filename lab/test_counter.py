"""
Test Cases for Counter Web Service

Requirements for the counter service
- The API must be RESTful.
- The endpoint must be called `/counters`.
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to get a counter's current value.
- The service must be able to delete a counter.
"""

from unittest import TestCase
from counter import app

class TestCounter(TestCase):
    #counter tests
    def test_create_counter(self): #what is self in python?
        #It should create a counter
        client = app.test_client()
        response = client.post("/counters/foo")
        self.assertEqual(response.status_code(201)) #assertEquals is deprecated lol
        data = response.get_json()
        self.assertEqual(data["name"],"foo")
        self.assertEqual(data["counter"],0)

