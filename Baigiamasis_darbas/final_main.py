from PyQt6.QtWidgets import QApplication, QMainWindow
from final_project import Ui_MainWindow
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import csv
import os




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_Button.clicked.connect(self.collect_inputs)

    def collect_inputs(self):
        url = self.ui.lineEdit.text()
        options = Options()
        options.add_argument('--incognito')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options)
        driver.get(url) 


        if "https://elenta.lt/" in url:
            total_amount = 0
            with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Price'])
                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")

                category = html.select_one("span[itemprop='itemListElement'] > span[itemprop='name']")
                category = category.text.strip().replace("»", "")

                number = html.select_one(".counter")
                number = number.text.strip()

                while True:

                    agree_button = driver.find_elements(By.CSS_SELECTOR, '.fc-button-label')
                    if agree_button:
                        agree_button[0].click()

                    
                    for box in html.select(".units-list li"):
                        if box:    

                            title = box.select_one(".ad-hyperlink")
                            title = title.text.strip() if title else "Nenurodyta"

                            price = box.select_one(".price-box")
                            price = price.text.strip() if price else "0"
                            writer.writerow([title, price])
                            print(f"Title: {title}, Price: {price}")
                            price = price.replace("€", "").replace(" ", "")
                            total_amount += int(price)
                            

                    next_button = driver.find_elements(By.CSS_SELECTOR, 'li.pagerNextPage')
                    if next_button:
                        next_button[0].click()
                        source = driver.page_source
                        html = BeautifulSoup(source, "html.parser")     
                        sleep(1)
                    else:
                        break      
            driver.quit()
            self.ui.feedback_label.setText(f"Kategorijoje:\n{category} yra {number} skelbimai/as\nBendra kainų suma yra {str(total_amount)}€")


        else:
            self.ui.feedback_label.setText(f"{url} netinkamas web puslapis") 
 


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Vobalis' Final Project")
    window.show()
    app.exec()


    