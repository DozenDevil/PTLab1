# -*- coding: utf-8 -*-
import numpy as np
from Types import RatingsType


class CalcSecondQuartile:

    def __init__(self, ratings: RatingsType) -> None:
        self.ratings: RatingsType = ratings
        self.second_quartile_students: list[str] = []

    def calc(self) -> list[str]:
        # Извлекаем рейтинги и вычисляем квартили
        rating_values = np.array(list(self.ratings.values()))
        q1 = np.percentile(rating_values, 25)
        q2 = np.percentile(rating_values, 50)

        # Определяем границы второй квартиль (Q1 и Q2)
        lower_bound = q1
        upper_bound = q2

        # Ищем студентов, попадающих во вторую квартиль
        self.second_quartile_students = [
            student for student, rating in self.ratings.items()
            if lower_bound < rating <= upper_bound
        ]

        return self.second_quartile_students
