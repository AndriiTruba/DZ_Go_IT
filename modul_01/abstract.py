from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass


class JsonData(SerializationInterface):
    def save(self, data):
        with open('file_name', 'w') as fh:
            json.dump(data, fh)


class BinData(SerializationInterface):
    def save(self, data):
        with open('file_name', 'wb') as fh:
            pickle.dump(data, fh)