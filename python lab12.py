import json

# Дані для записника (приклад)
data = {
    "contacts": [
        {"surname": "Litsman", "phone": "144-466-759"},
        {"surname": "Ivanov", "phone": "231-112-330"},
        {"surname": "Magamed", "phone": "315-629-202"},
        {"surname": "Zelenskiy", "phone": "446-761-000"},
        {"surname": "Goloborodko", "phone": "881-674-751"},
        {"surname": "Baranova", "phone": "681-981-666"},
        {"surname": "Bandera", "phone": "722-773-321"},
        {"surname": "Poroshenko", "phone": "877-131-474"},
        {"surname": "Kravchyk", "phone": "925-555-575"},
        {"surname": "Kluchko", "phone": "066-373-221"}
    ]
}
def show_all_contacts():
    if not data["contacts"]:
        return "Список контактів порожній."
    contacts_str = "Список контактів:\n"
    for contact in data["contacts"]:
        contacts_str += f"{contact['surname']}: {contact['phone']}\n"
    return contacts_str

def save_contacts(data):
    with open('contacts.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
def add_contact(surname, phone):

    # Перевіряємо, чи контакт з таким прізвищем або телефоном вже існує
    for contact in data["contacts"]:
        if contact["surname"] == surname:
            return f"Контакт з прізвищем {surname} вже існує."
        if contact["phone"] == phone:
            return f"Контакт з номером телефону {phone} вже існує."
    
    # Додаємо новий контакт
    data["contacts"].append({"surname": surname, "phone": phone})
    save_contacts(data)  # Зберігаємо зміни в файлі
    return f"Контакт {surname} з номером {phone} додано."


# Зберігаємо дані у JSON-файл
with open('contacts.json', 'w') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Функція для перевірки наявності телефону за прізвищем
def find_phone_by_surname(surname):
    for contact in data["contacts"]:
        if contact["surname"] == surname:
            return f"Телефон {surname}: {contact['phone']}"
    return f"Телефон для {surname} не знайдено."

# Функція для перевірки наявності прізвища за телефоном
def find_surname_by_phone(phone):
    for contact in data["contacts"]:
        if contact["phone"] == phone:
            return f"Власник телефону {phone}: {contact['surname']}"
    return f"Людину з номером {phone} не знайдено."

# Головне меню
def main_menu():
    while True:
        print("\nМеню:")
        print("1. Знайти номер телефону за прізвищем")
        print("2. Знайти прізвище за номером телефону")
        print("3. Додати новий контакт")
        print("4. Показати всі контакти")
        print("5. Вийти")
        
        choice = input("Виберіть опцію (1-5): ")
        
        if choice == '1':
            surname = input("Введіть прізвище: ")
            print(find_phone_by_surname(surname))
        elif choice == '2':
            phone = input("Введіть номер телефону: ")
            print(find_surname_by_phone(phone))
        elif choice == '3':
            surname = input("Введіть прізвище: ")
            phone = input("Введіть номер телефону: ")
            print(add_contact(surname, phone))
        elif choice == '4':
            print(show_all_contacts())
        elif choice == '5':
            print("Вихід з програми.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

# Запуск програми
if __name__ == "__main__":
    main_menu()