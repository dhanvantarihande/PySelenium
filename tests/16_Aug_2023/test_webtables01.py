from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    # LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    # # Find How Many Rows and
    # # XPATH of Rows = //*[@id="customers"]/tbody
    # row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr")
    # row = len(row_elements)
    # print(row)
    #
    # # How Many Columns That Have
    # # // *[ @ id = "customers"] / tbody / tr[2]
    # col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    # col = len(col_elements)
    # print(col)
    #
    # # FP -- //table[contains(@id,"cust")]/tbody/tr[
    # # 7
    # # SC -- ]/td[
    # # 3
    # # TP -- ]
    #
    # first_part = "//table[contains(@id,'cust')]/tbody/tr["
    # second_part = "]/td["
    # third_part = "]"
    #
    # for i in range(2, row + 1):
    #     for j in range(1, col + 1):
    #         dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
    #         print(dynamic_path)
    #         data = driver.find_element(By.XPATH, dynamic_path).text
    #         if "Helen Bennett" in data:
    #             country_path = f"{dynamic_path}/following-sibling::td"
    #             country_text = driver.find_element(By.XPATH, country_path).text
    #             print("Helen Bennett is in {country_text}")

    # Find Helen Bennett's Country

    driver.get("https://awesomeqa.com/webtable1.html")
    table = driver.find_element(By.XPATH, "//table[@summary= 'Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for e in cols:
            print(e.text)
