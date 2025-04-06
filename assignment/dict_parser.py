class DictParser:
  def __init__(self, object: dict):
    self.object = object

  def get_value_by_key(self, key: str, default_value = None):
    if isinstance(key, str) == False:
      raise TypeError('Key type must be string')
    try:
      value = self.__get_value_by_key(self.object, key, default_value)
    except KeyError:
      value = default_value
    return value

  def __get_value_by_key(self, object: dict, key: str, default_value):
    if not isinstance(object, dict):
      return default_value
    index = key.find('/')
    if index >= 0:
      first_key = key[:index]
      other_key = key[index + 1:]
      if len(first_key.strip()) == 0 or len(other_key.strip()) == 0:
        raise ValueError('Invalid key format')
      value = object[first_key]
      return self.__get_value_by_key(value, other_key, default_value)
    else:
      return object[key]