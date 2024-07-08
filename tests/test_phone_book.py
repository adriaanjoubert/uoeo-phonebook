from unittest import TestCase

from main import Entry, PhoneBook


class InsertTestCase(TestCase):

    def test_new_phone_book(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='B', phone_number='+2')
        phone_book.insert(entry=entry_2)
        self.assertCountEqual(
            first=phone_book.entries,
            second=[
                entry_1,
                entry_2,
            ],
        )


class DeleteTestCase(TestCase):

    def test_new_phone_book_delete_first_entry(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='B', phone_number='+2')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='C', phone_number='+3')
        phone_book.insert(entry=entry_3)
        phone_book.delete(id_=entry_1.id)
        self.assertCountEqual(
            first=phone_book.entries,
            second=[
                entry_2,
                entry_3,
            ],
        )
        self.assertDictEqual(
            d1=phone_book.index,
            d2={
                entry_2.id: 0,
                entry_3.id: 1,
            },
        )

    def test_new_phone_book_delete_middle_entry(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='B', phone_number='+2')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='C', phone_number='+3')
        phone_book.insert(entry=entry_3)
        phone_book.delete(id_=entry_2.id)
        self.assertCountEqual(
            first=phone_book.entries,
            second=[
                entry_1,
                entry_3,
            ],
        )
        self.assertDictEqual(
            d1=phone_book.index,
            d2={
                entry_1.id: 0,
                entry_3.id: 1,
            },
        )

    def test_new_phone_book_delete_last_entry(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='B', phone_number='+2')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='C', phone_number='+3')
        phone_book.insert(entry=entry_3)
        phone_book.delete(id_=entry_3.id)
        self.assertCountEqual(
            first=phone_book.entries,
            second=[
                entry_1,
                entry_2,
            ],
        )
        self.assertDictEqual(
            d1=phone_book.index,
            d2={
                entry_1.id: 0,
                entry_2.id: 1,
            },
        )
