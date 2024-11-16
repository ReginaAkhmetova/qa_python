import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
    #     # создаем экземпляр (объект) класса BooksCollector
    #     collector = BooksCollector()
    #
    #     # добавляем две книги
    #     collector.add_new_book('Гордость и предубеждение и зомби')
    #     collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    #
    #     # проверяем, что добавилось именно две
    #     # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
    #     assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # добавляет книги, длиной менее или равной 40 символов
    @pytest.mark.parametrize(
        'name',
        [
            'Питер Пен',
            'Приключения Гулливера',
            'Что делать, если ваш кот хочет вас убить',
        ]
    )
    def test_add_new_book_len_le_40_smb(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre
        assert len(collector.books_genre) == 1

    # добавляет книги, длиной более 40 символов
    @pytest.mark.parametrize(
        'name',
        [
            'Девушка, которая взрывала воздушные замки',
            'Жизнь и удивительные приключения Робинзона Крузо, моряка из Йорка, написанная им самим',
        ]
    )
    def test_add_new_book_len_gt_40_smb(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # устанавливает жанр книги
    @pytest.mark.parametrize(
        'name,genre',
        [
            ('Адвокат киллера', 'Детективы'),
            ('Оно', 'Ужасы')
        ]
    )
    def test_set_book_genre_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    # выводит список книг по жанру
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Тупой и еще тупее')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Тупой и еще тупее', 'Комедии')
        testval = collector.get_books_with_specific_genre('Ужасы')
        assert type(testval) is list
        assert len(testval) == 1

    # проверяет, что неправильный жанр не добавится
    def test_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'КакаятоФигня')
        assert collector.get_book_genre('Оно') == ''

    # выводит текущий словарь
    def test_get_books_genre(self):
        collector = BooksCollector()
        books_genre = {
            'Убийство на улице Морг': 'Ужасы',
            'Дракула': 'Ужасы',
            'Кот в сапогах': 'Мультфильмы'
        }
        for name, genre in books_genre.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == books_genre

    # возвращает книги, которые подходят детям
    def test_get_books_for_children(self):
        collector = BooksCollector()
        books_genre = {
            'Убийство на улице Морг': 'Ужасы',
            'Дракула': 'Ужасы',
            'Кот в сапогах': 'Мультфильмы'
        }
        for name, genre in books_genre.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Кот в сапогах']

    # добавляет книгу в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        assert 'Кот в сапогах' in collector.favorites

    # добавляет повторно ту же книгу в избранное
    def test_add_book_in_favorites_same_names(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        assert len(collector.get_list_of_favorites_books()) == 1

    # удаляет книгу из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        assert 'Кот в сапогах' in collector.favorites
        collector.delete_book_from_favorites('Кот в сапогах')
        assert 'Кот в сапогах' not in collector.favorites

    # получает список избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кот в сапогах')
        collector.add_book_in_favorites('Кот в сапогах')
        assert collector.get_list_of_favorites_books() == ['Кот в сапогах']
