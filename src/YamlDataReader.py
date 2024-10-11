# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        # Открываем и загружаем YAML-файл
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        # Проходим по загруженным данным
        for student in data:
            for name, subjects in student.items():
                # Создаём запись для студента
                self.students[name] = []
                # Добавляем предметы и оценки в список
                for subj, score in subjects.items():
                    self.students[name].append((subj, score))

        return self.students
