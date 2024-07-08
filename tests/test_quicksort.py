from unittest import TestCase

from main import Entry, PhoneBook


class QuicksortTestCase(TestCase):

    def test_empty(self) -> None:
        phone_book = PhoneBook()
        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[],
        )

    def test_length_1(self) -> None:
        phone_book = PhoneBook()
        entry = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry)
        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[entry],
        )

    def test_descending(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='Z', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='Y', phone_number='+1')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='X', phone_number='+1')
        phone_book.insert(entry=entry_3)
        entry_4 = Entry(name='W', phone_number='+1')
        phone_book.insert(entry=entry_4)
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_1,
                entry_2,
                entry_3,
                entry_4,
            ],
        )

        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_4,
                entry_3,
                entry_2,
                entry_1,
            ],
        )

    def test_ascending(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='B', phone_number='+1')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='C', phone_number='+1')
        phone_book.insert(entry=entry_3)
        entry_4 = Entry(name='D', phone_number='+1')
        phone_book.insert(entry=entry_4)
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_1,
                entry_2,
                entry_3,
                entry_4,
            ],
        )

        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_1,
                entry_2,
                entry_3,
                entry_4,
            ],
        )

    def test_random(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='C', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='D', phone_number='+1')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_3)
        entry_4 = Entry(name='B', phone_number='+1')
        phone_book.insert(entry=entry_4)
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_1,
                entry_2,
                entry_3,
                entry_4,
            ],
        )

        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_3,
                entry_4,
                entry_1,
                entry_2,
            ],
        )

    def test_dirty(self) -> None:
        phone_book = PhoneBook()
        entry_1 = Entry(name='A', phone_number='+1')
        phone_book.insert(entry=entry_1)
        entry_2 = Entry(name='C', phone_number='+1')
        phone_book.insert(entry=entry_2)
        entry_3 = Entry(name='B', phone_number='+1')
        phone_book.insert(entry=entry_3)
        entry_4 = Entry(name='D', phone_number='+1')
        phone_book.insert(entry=entry_4)
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_1,
                entry_2,
                entry_3,
                entry_4,
            ],
        )

        phone_book.delete(id_=1)
        phone_book.sort()
        self.assertListEqual(
            list1=phone_book.entries,
            list2=[
                entry_3,
                entry_2,
                entry_4,
            ],
        )
