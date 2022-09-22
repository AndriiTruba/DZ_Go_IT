from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass


class JsonData(SerializationInterface):
    def save(self, data):
        with open('file_name.json', 'w') as fh:
            json.dump(data, fh)
        print(f'{fh} has been saved')


class BinData(SerializationInterface):
    def save(self, data):
        with open('file_name.bin', 'wb') as fh:
            pickle.dump(data, fh)
        print(f'{fh} has been saved')