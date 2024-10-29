class AUTO:
    def __init__(self, model, manufacturer, year):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year

    def set_year(self, year):
        self.year = year

    def display_info(self):
        print(f"Модель: {self.model}, Виробник: {self.manufacturer}, Рік випуску: {self.year}")


def add_auto_to_list(auto_list, model, manufacturer, year):
    auto = AUTO(model, manufacturer, year)
    auto_list.append(auto)


def display_auto_list(auto_list):
    if not auto_list:
        print("Список автомобілів порожній.")
    else:
        for auto in auto_list:
            auto.display_info()


def search_auto_by_model(auto_list, model):
    for auto in auto_list:
        if auto.model == model:
            print("Автомобіль знайдено:")
            auto.display_info()
            return auto
    print("Автомобіль не знайдено.")
    return None

if __name__ == "__main__":
    auto_list = []

    N = int(input("Скільки автомобілів додати до списку? "))
    for _ in range(N):
        model = input("Введіть модель автомобіля: ")
        manufacturer = input("Введіть виробника автомобіля: ")
        year = int(input("Введіть рік випуску автомобіля: "))
        add_auto_to_list(auto_list, model, manufacturer, year)

    print("\n")
    print("Список усіх автомобілів:")
    display_auto_list(auto_list)

    print("\n")
    search_model = input("Введіть модель для пошуку: ")
    search_auto_by_model(auto_list, search_model)
