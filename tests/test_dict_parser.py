import pytest
from assignment.dict_parser import DictParser

@pytest.fixture
def nested_object():
  return {
    "a": {
      "b": {
        "c": "x",
        "d": "10"
      },
      "e": "y"
    },
    "f": "z"
  }

@pytest.mark.parametrize("key, expected_value", [
  ('f', 'z'),
  ('a/e', 'y'),
  ('a/b/c', 'x'),
  ('a/b/d', '10'),
  ('a/b', { "c": "x", "d": "10"}),
  ('a/b/d/e/f', None),
])
def test_get_value_by_key(nested_object, key, expected_value):
  parser = DictParser(nested_object)
  value = parser.get_value_by_key(key)
  assert expected_value == value

@pytest.mark.parametrize("key, expected_error_type, expected_error_message", [
  ('/a/b/c', ValueError, 'Invalid key format'),
  ('a/b//c', ValueError, 'Invalid key format'),
  ('a/b/ /c', ValueError, 'Invalid key format'),
  ('a/b/c/', ValueError, 'Invalid key format'),
  ('a/b/ ', ValueError, 'Invalid key format'),
  (123, TypeError, 'Key type must be string'),
])
def test_get_value_by_invalid_key(nested_object, key, expected_error_type, expected_error_message):
  parser = DictParser(nested_object)
  with pytest.raises(expected_error_type) as err_info:
    parser.get_value_by_key(key)
  assert str(err_info.value) == expected_error_message
  