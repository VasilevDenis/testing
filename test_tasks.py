import pytest

import secret
import task1
import task2
import task3
from yandex_uploader import YaUploader

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]


class TestTask:
    @pytest.mark.parametrize("test_input,expected", [(mentors, 292), ])
    def test_task1(self, test_input, expected):
        assert len(task1.get_unique_names(test_input)) == expected

    @pytest.mark.parametrize("test_input,expected", [((task2.courses, task2.mentors, task2.durations),
                                                      'Самый короткий курс(ы): Python-разработчик'
                                                      ' с нуля - 12 месяца(ев)'
                                                      'Самый длинный курс(ы): Fullstack-разработчик на Python,'
                                                      ' Frontend-разработчик с нуля - 20 месяца(ев)'), ])
    def test_task2(self, test_input, expected):
        result = task2.get_shortest_and_longest_course(*test_input)
        assert result == expected

    @pytest.mark.parametrize("test_input,expected", [(task3.mentors, 292), ])
    def test_task3(self, test_input, expected):
        result = task3.get_top3(test_input)
        assert '10' in result
        assert '4' in result
        assert '5' in result

    def test_yandex(self):
        uploader = YaUploader(secret.token)
        folder_path = 'test2'
        upload_status = uploader.create_folder(folder_path)
        assert upload_status == 201
        check_status = uploader.check_folder(folder_path)
        assert check_status == 200





