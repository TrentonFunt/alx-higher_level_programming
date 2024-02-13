#!/usr/bin/python3
"""Base module"""
import json
import csv
import os.path


class Base:
    """
    Base class representing the base functionality for other classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instances of Base.

        Args:
            id (int, optional): The ID of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries into a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects into a JSON file.

        Args:
            list_objs (list): List of instances to be saved.
        """
        filename = f"{cls.__name__}.json"
        list_dic = []

        if list_objs:
            list_dic = [obj.to_dictionary() for obj in list_objs]

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string into a list of dictionaries.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance using a dictionary of attributes.

        Args:
            dictionary (dict): Dictionary of attributes.

        Returns:
            Base: Instance of the class.
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = [cls.create(**lst) for lst in list_cls]

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects into a CSV file.

        Args:
            list_objs (list): List of instances to be saved.
        """
        filename = f"{cls.__name__}.csv"

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if list_objs:
            for obj in list_objs:
                matrix.append([getattr(obj, key) for key in list_keys])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        list_ins = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            list_ins.append(cls.create(**dict_csv))

        return list_ins
