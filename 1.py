class Child:
    def __init__(self, name, age):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя ребенка должно быть непустой строкой")
        if not isinstance(age, int) or age < 0 or age > 18:
            raise ValueError("Возраст ребенка должен быть целым числом от 0 до 18")

        self.name = name.strip()
        self.age = age
        self.is_calm = False
        self.is_hungry = True

    def __str__(self):
        return (f"Ребенок: {self.name}, возраст: {self.age}, "
                f"состояние спокойствия: {'Спокоен' if self.is_calm else 'Не спокоен'}, "
                f"состояние голода: {'Голодный' if self.is_hungry else 'Сытый'}")


class Parent:
    def __init__(self, name, age):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Имя родителя должно быть непустой строкой")
        if not isinstance(age, int) or age < 16:
            raise ValueError("Возраст родителя должен быть целым числом не меньше 16")

        self.name = name.strip()
        self.age = age
        self.children = []

    def add_child(self, child):
        if not isinstance(child, Child):
            raise ValueError("Можно добавить только объект класса Child")

        if self.age - child.age < 16:
            raise ValueError("Разница в возрасте между родителем и ребенком должна быть не менее 16 лет")

        self.children.append(child)

    def __str__(self):
        return (f"Родитель: {self.name}, возраст: {self.age}, "
                f"количество детей: {len(self.children)}")

    def calm_child(self, child_index):
        if not isinstance(child_index, int) or not (0 <= child_index < len(self.children)):
            raise IndexError("Ребёнка с таким индексом не существует.")

        self.children[child_index].is_calm = True
        print(f"Родитель {self.name} успокоил ребенка {self.children[child_index].name}")

    def feed_child(self, child_index):
        if not isinstance(child_index, int) or not (0 <= child_index < len(self.children)):
            raise IndexError("Ребёнка с таким индексом не существует.")

        self.children[child_index].is_hungry = False
        print(f"Родитель {self.name} накормил ребенка {self.children[child_index].name}")


def validate_name(name):
    name = name.strip()
    if not name:
        raise ValueError("Имя не может быть пустым")
    if not all(c.isalpha() or c.isspace() or c in "-'" for c in name):
        raise ValueError("Имя должно содержать только буквы, пробелы, дефисы и апострофы")
    if len(name) < 2:
        raise ValueError("Имя должно содержать минимум 2 символа")
    return name


def validate_parent_age(age_str):
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Возраст должен быть целым числом")

    if age < 16:
        raise ValueError("Минимальный возраст родителя - 16 лет")
    return age


def validate_child_age(age_str):
    try:
        age = int(age_str)
    except ValueError:
        raise ValueError("Возраст должен быть целым числом")

    if age < 0 or age > 18:
        raise ValueError("Возраст ребенка должен быть от 0 до 18 лет")
    return age


def validate_positive_int(value_str, max_value=None):
    try:
        value = int(value_str)
    except ValueError:
        raise ValueError("Должно быть целым числом")

    if value <= 0:
        raise ValueError("Должно быть положительным числом")
    if max_value is not None and value > max_value:
        raise ValueError(f"Должно быть не больше {max_value}")
    return value


def input_with_validation(prompt, validation_func, error_message=None):
    while True:
        try:
            value = input(prompt)
            validated_value = validation_func(value)
            return validated_value
        except ValueError as e:
            print(f"Ошибка: {error_message or str(e)}")
            print("Пожалуйста, попробуйте еще раз.\n")


def create_child(parent_age):
    while True:
        try:
            name = input_with_validation(
                "Введите имя ребенка: ",
                validate_name,
                "Имя должно содержать только буквы, пробелы, дефисы и апострофы (минимум 2 символа)"
            )
            age = input_with_validation(
                "Введите возраст ребенка: ",
                validate_child_age,
                "Возраст ребенка должен быть от 0 до 18 лет"
            )

            child = Child(name, age)

            if parent_age - age < 16:
                print(f"Ошибка: Разница в возрасте между родителем и ребенком должна быть не менее 16 лет.")
                print(f"Родителю {parent_age} лет, ребенку {age} лет - разница {parent_age - age} лет.")
                print("Пожалуйста, введите данные ребенка снова.")
                continue

            return child
        except ValueError as e:
            print(f"Ошибка при создании ребенка: {str(e)}")
            print("Пожалуйста, попробуйте еще раз.\n")


def select_parent(parents):
    if not parents:
        print("Нет доступных родителей.")
        return None

    while True:
        try:
            print("\nСписок родителей:")
            for i, parent in enumerate(parents, 1):
                print(f"{i}. {parent.name} ({parent.age} лет), детей: {len(parent.children)}")

            choice = input_with_validation(
                "Выберите номер родителя (или 0 для отмены): ",
                lambda x: validate_positive_int(x, len(parents)),
                f"Введите число от 1 до {len(parents)}"
            )

            if choice == 0:
                return None
            return parents[choice - 1]
        except Exception as e:
            print(f"Ошибка: {str(e)}")


def select_child(parent):
    if not parent.children:
        print(f"У родителя {parent.name} нет детей.")
        return None

    while True:
        try:
            print(f"\nДети родителя {parent.name}:")
            for i, child in enumerate(parent.children, 1):
                print(f"{i}. {child}")

            choice = input_with_validation(
                "Выберите номер ребенка (или 0 для отмены): ",
                lambda x: validate_positive_int(x, len(parent.children)),
                f"Введите число от 1 до {len(parent.children)}"
            )

            if choice == 0:
                return None
            return choice - 1
        except Exception as e:
            print(f"Ошибка: {str(e)}")


def main():
    parents = []

    print("=== Создание родителей ===")
    num_parents = input_with_validation(
        "Введите количество родителей: ",
        lambda x: validate_positive_int(x, 10),
        "Количество родителей должно быть положительным числом (максимум 10)"
    )

    for i in range(num_parents):
        print(f"\n=== Родитель {i + 1}/{num_parents} ===")
        parent_name = input_with_validation(
            "Введите имя родителя: ",
            validate_name,
            "Имя должно содержать только буквы, пробелы, дефисы и апострофы (минимум 2 символа)"
        )
        parent_age = input_with_validation(
            "Введите возраст родителя: ",
            validate_parent_age,
            "Возраст родителя должен быть целым числом не меньше 16"
        )

        parent = Parent(parent_name, parent_age)

        num_children = input_with_validation(
            f"Введите количество детей у родителя {parent_name}: ",
            lambda x: validate_positive_int(x),
            "Количество детей должно быть положительным числом"
        )

        for j in range(num_children):
            print(f"\n--- Ребенок {j + 1}/{num_children} родителя {parent_name} ---")
            child = create_child(parent_age)
            parent.add_child(child)

        parents.append(parent)
        print(f"\nРодитель {parent_name} успешно добавлен!")

    while True:
        print("\n=== Главное меню ===")
        print("1. Просмотреть информацию о родителе")
        print("2. Просмотреть информацию о детях родителя")
        print("3. Успокоить ребенка")
        print("4. Покормить ребенка")
        print("5. Выход")

        choice = input_with_validation(
            "Выберите действие (1-5): ",
            lambda x: validate_positive_int(x, 5),
            "Введите число от 1 до 5"
        )

        if choice == 1:
            parent = select_parent(parents)
            if parent:
                print("\nИнформация о родителе:")
                print(parent)

        elif choice == 2:
            parent = select_parent(parents)
            if parent:
                if not parent.children:
                    print(f"\nУ родителя {parent.name} нет детей.")
                else:
                    print(f"\nДети родителя {parent.name}:")
                    for i, child in enumerate(parent.children, 1):
                        print(f"{i}. {child}")

        elif choice == 3:
            parent = select_parent(parents)
            if parent:
                child_index = select_child(parent)
                if child_index is not None:
                    try:
                        parent.calm_child(child_index)
                    except Exception as e:
                        print(f"Ошибка: {str(e)}")

        elif choice == 4:
            parent = select_parent(parents)
            if parent:
                child_index = select_child(parent)
                if child_index is not None:
                    try:
                        parent.feed_child(child_index)
                    except Exception as e:
                        print(f"Ошибка: {str(e)}")

        elif choice == 5:
            print("\nПрограмма завершена. До свидания!")
            break

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
