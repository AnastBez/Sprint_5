import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_add_have_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Комедии')
        assert ('Гордость и предубеждение и зомби' in collector.books_genre.keys() and
                'Комедии' in collector.books_genre.values())

    def test_set_book_genre_not_have_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Мелодрамма')
        assert 'Комедии' not in collector.books_genre.values()

    def test_get_book_genre_have_genre(self):
        collector = BooksCollector()
        assert 'Детективы' in collector.genre

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Гордость и предубеждение и зомби', 'Детективы'],
            ['Что делать, если ваш кот хочет вас убить', 'Комедии']
        ]
    )
    def test_get_book_genre_have_not_genre(self, name, genre):
        collector = BooksCollector()
        assert 'Отстой' not in collector.genre

    def test_get_books_with_specific_genre_search_one_genre_have_two_values(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Гордость и предубеждение и зомби': 'Детективы',
            'Что делать, если ваш кот хочет вас убить': 'Комедии',
            'Сверхъестественное': ' ',
            'Бриллиантовая нога': 'Комедии'
             }
        assert len(collector.get_books_with_specific_genre('Комедии')) >= 2

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.books_genre = {}
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Мэри Поппинс', 'Фантастика'],
            ['Винни Пух и приключения', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_age_rating_not_in_child_books(self, name, genre):
        collector = BooksCollector()
        collector.genre_age_rating = ['Ужасы', 'Детективы']
        for i in collector.genre_age_rating:
            assert i not in genre

    def test_add_book_in_favorites_add_one_book_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {'Что делать, если ваш кот хочет вас убить': 'Фантастика'}
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.favorites

    def test_delete_book_from_favorites_if_book_in_favorites(self):
        collector = BooksCollector()
        collector.favorites = ['Что делать, если ваш кот хочет вас убить']
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' not in collector.favorites

    @pytest.mark.parametrize(
        'name',
        [
            'Гордость и предубеждение и зомби',
            'Что делать, если ваш кот хочет вас убить',
            'Сверхъестественное',
            'Бриллиантовая нога'

        ]
    )
    def test_get_list_of_favorites_books_if_list_not_empty(self, name):
        collector = BooksCollector()
        collector.favorites = name
        assert len(collector.get_list_of_favorites_books()) != 0
