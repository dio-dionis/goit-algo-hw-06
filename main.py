from collections import UserDict

class Field:
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Ім'я є обов'язковим полем, логіка ініціалізації вже в Field
    pass

class Phone(Field):
    def __init__(self, value):
    # Номер має складатися рівно з 10 цифр    
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must consist of 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Створюємо об'єкт Phone і додаємо до списку
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Шукаємо телефон за значенням і видаляємо його
        p = self.find_phone(phone)
        if p:
            self.phones.remove(p)
            return
        raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        # Знаходимо старий номер, якщо його немає - генеруємо помилку
        p = self.find_phone(old_phone)
        if p:
            self.phones[self.phones.index(p)] = Phone(new_phone)
            return
        raise ValueError("Old phone not found")

    def find_phone(self, phone):
        # Шукаємо об'єкт Phone у списку за значенням value
        phone_value = phone.value if isinstance(phone, Phone) else phone
        for p in self.phones:
            if p.value == phone_value:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        # Додаємо запис, використовуючи ім'я як ключ
        self.data[record.name.value] = record

    def find(self, name):
        # Повертає Record або None
        return self.data.get(name)

    def delete(self, name):
        # Видаляємо запис за ключем (ім'ям)
        if name in self.data:
            del self.data[name]

    def __str__(self): 
        # Красивий вивід всієї книги
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())


# Перевірка працездатності коду
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone('1234567890')
    john_record.add_phone('5555555555')

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone('9876543210')
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("--- All Records ---")
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone('1234567890', '1112223333')
        print("\n--- After editing John's phone ---")
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone('5555555555')
    print(f"\nSearch result: {john.name.value}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print("\n--- After deleting Jane ---")
    print(book)
    

   