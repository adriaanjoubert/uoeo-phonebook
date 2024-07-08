COMMANDS = """
1. Add a new entry
2. Print all entries
3. Search for an entry by ID
4. Sort entire phonebook by name
5. Delete entry by ID
6. Exit
"""


class Entry:
    id: int
    name: str
    phone_number: str

    def __init__(self, name: str, phone_number: str) -> None:
        self.name = name
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone_number}'


class PhoneBook:

    def __init__(self) -> None:
        self.entries: list[Entry] = []
        self.entry_id = self.generate_id()
        self.index: dict[int, int] = {}
        self.length = 0

    def __str__(self) -> str:
        representation = ""
        for entry in self.entries:
            representation += f"{entry}\n"
        return representation

    @staticmethod
    def generate_id() -> int:
        i = 0
        while True:
            i += 1
            yield i

    def insert(self, entry: Entry) -> None:
        # We insert a new entry by appending it to the list of existing entries.
        entry.id = next(self.entry_id)
        self.entries.append(entry)
        self.index[entry.id] = self.length
        self.length += 1

    def delete(self, id_: int) -> bool:
        # Since we are keeping track of the index of every entry in the list, we can implement deletion by creating
        # a new list of entries consisting of the parts of the old list before and after the entry to be deleted.
        try:
            index = self.index[id_]
            new_entries = self.entries[:index]
            if index < self.length:
                new_entries += self.entries[index + 1:]
                for entry in new_entries[index:]:
                    self.index[entry.id] -= 1
            self.entries = new_entries
            del self.index[id_]
            self.length -= 1
            return True
        except KeyError:
            # Entry with that ID not found.
            return False

    def sort(self) -> None:
        quicksort(entries=self.entries, left=0, right=self.length - 1, index=self.index)


def quicksort(entries: list[Entry], left: int, right: int, index: dict[int, int]) -> None:
    """
    From Sedgewick (1992). Algorithmen in C++. Bonn: Addison-Wesley.
    """
    if right <= left:
        return
    pivot = entries[right]
    i = left
    j = right
    while True:
        while True:
            if entries[i].name < pivot.name:
                i += 1
            else:
                break
        while True:
            if entries[j].name > pivot.name:
                j -= 1
            else:
                break
        if i >= j:
            break
        entries[i], entries[j] = entries[j], entries[i]

        # We need to update the index to reflect the new positions of the entries.
        index[entries[i].id], index[entries[j].id] = index[entries[j].id], index[entries[i].id]
    quicksort(entries=entries, left=left, right=i - 1, index=index)
    quicksort(entries=entries, left=i + 1, right=right, index=index)


def main() -> None:
    phone_book = PhoneBook()

    while True:
        print(COMMANDS)
        match input("Enter command (1-6): "):
            case '1':
                # Add entry
                name = input("\nName: ")
                phone_number = input("Phone number: ")
                entry = Entry(name=name, phone_number=phone_number)
                phone_book.insert(entry=entry)
                print(f"\nEntry added: {entry}")
            case '2':
                # Print all entries
                print()
                print(phone_book)
            case '3':
                # Search for an entry by ID
                id_ = input("\nEnter ID: ")
                try:
                    id_ = int(id_)
                except ValueError:
                    print("\nInvalid ID: ", id_)
                    continue
                try:
                    index = phone_book.index[id_]
                except KeyError:
                    print("\nEntry not found")
                    continue
                print()
                print(phone_book.entries[index])
            case '4':
                # Sort phonebook
                phone_book.sort()
                print()
                print(phone_book)
            case '5':
                # Delete entry by ID
                id_ = input("\nEnter ID: ")
                try:
                    id_ = int(id_)
                except ValueError:
                    print("\nInvalid ID: ", id_)
                    continue
                phone_book.delete(id_)
                print()
                print(phone_book)
            case '6':
                # Exit
                break
            case _:
                print("\nInvalid command")


if __name__ == '__main__':
    main()
