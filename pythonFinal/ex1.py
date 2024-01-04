import json
import os

class FryChicken:
    def __init__(self, fryChicken, Fries, Soda, Salad, Flavor):
        self.setup = {}
        self._soda = Soda
        self._fries = Fries
        self._fryChicken = fryChicken
        self._salad = Salad
        self._flavor = Flavor

    def add_combo(self, easyCombo):
        for combo in easyCombo:
            self.setup.setdefault(combo[2], []).append({"main meal": combo[0], "Comes with meal": combo[1]})

    def delete_combo(self, setup_fryChicken, easyCombo):
        setup_easyCombo = self.setup.get(easyCombo, [])
        self.setup[easyCombo] = [_setup for _setup in setup_easyCombo if _setup["main meal"] != setup_fryChicken]
        print(f"Setup {setup_fryChicken} deleted for {self._fryChicken} in setup {easyCombo}.")

    def get_setup(self, easyCombo):
        return self.setup.get(easyCombo, [])

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump({"Main Meal": self._fryChicken, "Comes with meal": self._fries, "Soda": self._soda}, file)

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self._fryChicken, self._fries, self._soda = data.get("Main Meal"), data.get("Comes with meal"), data.get("Soda", {})

def create_or_load_student_profile(fryChicken, Fries, Cola, Salad, Flavor):
    setup_filename = f"{fryChicken}_profile.json"
    setup = FryChicken(fryChicken, Fries, Cola, Salad, Flavor)
    setup.load_from_file(setup_filename)
    return setup, setup_filename

def add_combo(setup, *easycombo):
    setup.add_combo(easycombo)

#顯示套餐
def display_setup(setup_fryChicken, setup_fries, setup_soda, easyCombo, setup_taken):
    print(f"Setup taken by {setup_fryChicken}, {setup_fries} , {setup_soda} in {easyCombo}:")
    for setup in setup_taken:
        print(f"{setup['main meal']}: {setup['Comes with meal']}")

def delete_and_save_course(setup, fryChicken, easyCombo):
    setup.delete_combo(fryChicken, easyCombo)
    setup.save_to_file(setup_filename)

# 使用參數
fryChicken = "wings"
Fries = "potato"
Soda = "cola"
Salad = "Salad"
Flavor = "hot"

# 建立餐點
setup, setup_filename = create_or_load_student_profile(fryChicken, Fries, Soda, Salad, Flavor)

# 添加餐點
setup_to_add = [("Comes with meal", "fries", "easycombo")]
add_combo(setup, *setup_to_add)

# 儲存至檔案
setup.save_to_file(setup_filename)

# 顯示特定 自由搭配 的餐點
setup_to_search = "easycombo"
courses_taken = setup.get_setup(setup_to_search)
display_setup(fryChicken, Fries, Soda, setup_to_search, courses_taken)

# 刪除餐點
course_to_delete = "main meal"
delete_and_save_course(setup, course_to_delete, setup_to_search)
