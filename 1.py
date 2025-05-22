class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_calm = False
        self.is_hungry = True

    def __str__(self):
        s = ""
        s += ("Ребенок: " + self.name + ", возраст: " + str(self.age) +
              ", состояние спокойствия: " + ("Спокоен" if self.is_calm else "Не спокоен") +
              ", состояние голода: " + ("Голодный" if self.is_hungry else "Сытый"))
        return s

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        s = ""
        s += ("Родитель: " + self.name + ", возраст: " + str(self.age) +
              ", количество детей: " + str(len(self.children)))
        return s

    def calm_child(self, child_index):
        if 0 <= child_index < len(self.children):
            self.children[child_index].is_calm = True
            print(f"Родитель {self.name} успокоил ребенка {self.children[child_index].name}")
        else:
            print("Ребёнка с таким индексом не существует.")

    def feed_child(self, child_index):
        if 0 <= child_index < len(self.children):
            self.children[child_index].is_hungry = False
            print(f"Родитель {self.name} накормил ребенка {self.children[child_index].name}")
        else:
            print("Ребёнка с таким индексом не существует.")

def main():
    parents = []
    num_parents = int(input("Введите количество родителей: "))

    for i in range(num_parents):
        parent_name = input(f"Введите имя родителя {i+1}: ")
        parent_age = int(input(f"Введите возраст родителя {i+1}: "))
        parent = Parent(parent_name, parent_age)

        num_children = int(input(f"Введите количество детей у родителя {parent_name}: "))
        for j in range(num_children):
            child_name = input(f"Введите имя ребенка {j+1}: ")
            child_age = int(input(f"Введите возраст ребенка {j+1}: "))
            child = Child(child_name, child_age)
            parent.add_child(child)

        parents.append(parent)

    while True:
        print("\nМеню:")
        print("1) Информация о родителе")
        print("2) Информация о всех детях данного родителя")
        print("3) Выполнить действие с ребенком")
        print("4) Выход")

        choice = int(input("Выберите действие: "))

        if choice == 1:
            k = int(input("Введите номер родителя: ".format(len(parents)))) - 1
            if 0 <= k < len(parents):
                print(parents[k].__str__())
            else:
                print("Некорректный номер родителя.")

        elif choice == 2:
            k = int(input("Введите номер родителя: ".format(len(parents)))) - 1
            if 0 <= k < len(parents):
                for i, child in enumerate(parents[k].children):
                    print(f"{i+1}. {child.__str__()}")
            else:
                print("Некорректный номер родителя.")

        elif choice == 3:
            k_parent = int(input("Введите номер родителя: ".format(len(parents)))) - 1
            k_child = int(input("Введите номер ребёнка: ".format(len(parents[k_parent].children)))) - 1

            action = input("Выберите действие (1 - успокоить, 2 - покормить): ")
            if action == "1":
                parents[k_parent].calm_child(k_child)
            elif action == "2":
                parents[k_parent].feed_child(k_child)
            else:
                print("Некорректный выбор действия.")

        elif choice == 4:
            print("Вы вышли из программы")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
