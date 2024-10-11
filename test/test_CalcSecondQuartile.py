# -*- coding: utf-8 -*-
import pytest
import numpy as np
from src.Types import RatingsType
from src.CalcSecondQuartile import CalcSecondQuartile


class TestCalcSecondQuartile:

    @pytest.fixture()
    def input_ratings(self) -> RatingsType:
        return {
            "Иванов": 60.0,
            "Кузнецов": 95.0,
            "Петров": 75.0,
            "Сидоров": 85.0,
            "Лебедев": 50.0,
            "Попов": 70.0,
            "Смирнов": 82.0
        }

    def test_calc(self, input_ratings: RatingsType) -> None:
        calc_quartile = CalcSecondQuartile(input_ratings)
        result = calc_quartile.calc()

        # Вычисление квартили для вывода
        rating_values = np.array(list(input_ratings.values()))
        q1 = np.percentile(rating_values, 25)
        q2 = np.percentile(rating_values, 50)

        expected = ["Петров", "Попов"]  # Ожидаемые студенты во второй квартиль
        assert sorted(result) == sorted(expected)
