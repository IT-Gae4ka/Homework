# Task 6.2
# Implement custom dictionary that will memorize 10 latest changed keys. Using method "get_history" return this keys.

# Example:

# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]

class HistoryDict:
    latest_keys_size = 10
    def __init__(self, input_dict = {}):
        self.input_dict = input_dict
        self.latest_keys = []

    def set_value(self, key, value):
        if len(self.latest_keys) == self.latest_keys_size:
            del self.latest_keys[0]
        if key not in self.latest_keys:
            self.latest_keys.append(key)

    def get_history(self):
        print(self.latest_keys)

d = HistoryDict({"foo": 42})
d.set_value("key1", 43)
d.set_value("key2", 43)
d.set_value("key3", 43)
d.set_value("key4", 43)
d.set_value("key5", 43)
d.set_value("key6", 43)
d.set_value("key7", 43)
d.set_value("key8", 43)
d.set_value("key9", 43)
d.set_value("key10", 43)
d.set_value("key11", 43)
d.set_value("key12", 43)

d.get_history()