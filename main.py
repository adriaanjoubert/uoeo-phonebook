COMMANDS = """
1. Add a new entry
2. Print all entries
3. Search for an entry
4. Sort entire phonebook by name
5. Delete entry by ID
"""


def generate_id() -> int:
    i = 0
    while True:
        i += 1
        yield i


entry_id = generate_id()


class Entry:
    id: int
    name: str
    phone_number: str

    def __init__(self, name: str, phone_number: str) -> None:
        self.id = next(entry_id)
        self.name = name
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phone_number}'


phonebook: list[Entry] = []


def main() -> None:
    while True:
        print(COMMANDS)
        match input("Enter command (1-10): "):
            case '1':
                # Add entry
                name = input("Name: ")
                phone_number = input("Phone number: ")
                phonebook.append(Entry(name=name, phone_number=phone_number))
            case '2':
                # Print all entries
                for entry in phonebook:
                    print(entry)
            case '3':
                # Search for an entry
                pass
            case '4':
                # Sort phonebook
                pass
            case '5':
                # Delete entry by ID
                pass


if __name__ == '__main__':
    main()
