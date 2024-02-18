# в рекомендаціях маємо from collections import UserDict
# в прикладі виконання AddressBook, тож не зрозумів, що саме маю вибрати, залишив поки що AddressBook

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not self.validate_phone(value):
            raise ValueError("Invalid phone number format")
        super().__init__(value)

    @staticmethod
    def validate_phone(phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook:
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        if name in self.data:
            del self.data[name]

    def find_record(self, name):
        return self.data.get(name)

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print("All records in the address book:")
print(book)

john = book.find_record("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    print("Updated John's record:")
    print(john)

if john:
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

book.delete_record("Jane")
print("Address book after deleting Jane's record:")
print(book)