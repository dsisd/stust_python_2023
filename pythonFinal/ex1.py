import json
import os

class FryChicken:
    def __init__(self, fryChicken, Fries, Soda, Salad, Flavor):
        # 初始化餐點設定
        self.setup = {}
        self._soda = Soda
        self._fries = Fries
        self._fryChicken = fryChicken
        self._salad = Salad
        self._flavor = Flavor

    def add_combo(self, easyCombo):
        # 添加套餐到設定中
        for combo in easyCombo:
            self.setup.setdefault(combo[2], []).append({"主餐": combo[0], "附餐": combo[1]})

    def delete_combo(self, setup_fryChicken, easyCombo):
        # 刪除特定套餐中的主餐
        setup_easyCombo = self.setup.get(easyCombo, [])
        self.setup[easyCombo] = [_setup for _setup in setup_easyCombo if _setup["主餐"] != setup_fryChicken]
        print(f"在 {easyCombo} 中，刪除 {self._fryChicken} 的設定 {setup_fryChicken}.")

    def get_setup(self, easyCombo):
        # 獲取特定套餐的設定
        return self.setup.get(easyCombo, [])

    def save_to_file(self, filename):
        # 將餐點設定儲存至檔案
        with open(filename, 'w') as file:
            json.dump({"主餐": self._fryChicken, "附餐": self._fries, "汽水": self._soda}, file)

    def load_from_file(self, filename):
        # 從檔案載入餐點設定
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self._fryChicken, self._fries, self._soda = data.get("主餐"), data.get("附餐"), data.get("汽水", {})

def create_or_load_meal(fryChicken, Fries, Cola, Salad, Flavor):
    # 創建或載入餐點
    setup_filename = f"{fryChicken}_profile.json"
    setup = FryChicken(fryChicken, Fries, Cola, Salad, Flavor)
    setup.load_from_file(setup_filename)
    return setup, setup_filename

def add_combo(setup, *easycombo):
    # 添加自由搭配餐點
    setup.add_combo(easycombo)

# 顯示套餐
def display_setup(setup_fryChicken, setup_fries, setup_soda, easyCombo, setup_taken):
    print(f"{easyCombo} 中的設定，由 {setup_fryChicken}、{setup_fries} 和 {setup_soda} 取得的套餐:")
    for setup in setup_taken:
        print(f"{setup['主餐']}: {setup['附餐']}")

def delete_and_save_course(setup, fryChicken, easyCombo):
    # 刪除餐點並儲存至檔案
    setup.delete_combo(fryChicken, easyCombo)
    setup.save_to_file(setup_filename)

# 使用參數
fryChicken = "wings"
Fries = "potato"
Soda = "cola"
Salad = "Salad"
Flavor = "hot"

# 建立或載入餐點
setup, setup_filename = create_or_load_meal(fryChicken, Fries, Soda, Salad, Flavor)

# 添加餐點
setup_to_add = [("附餐", "fries", "自由搭配")]
add_combo(setup, *setup_to_add)

# 儲存至檔案
setup.save_to_file(setup_filename)

# 顯示特定自由搭配的餐點
setup_to_search = "自由搭配"
courses_taken = setup.get_setup(setup_to_search)
display_setup(fryChicken, Fries, Soda, setup_to_search, courses_taken)

# 刪除餐點
course_to_delete = "主餐"
delete_and_save_course(setup, course_to_delete, setup_to_search)
