# Bibliotekos kurias naudojau:
from PyQt6.QtWidgets import QApplication, QMainWindow
from final_project import Ui_MainWindow
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
import csv




class MainWindow(QMainWindow):
    def __init__(self):
    #Sukuriamas progrramos UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start_Button.clicked.connect(self.collect_inputs)

    def collect_inputs(self):
        #Aktyvuojasi Start mygtukas kuris surenka input laukelyje esanti url.
        url = self.ui.lineEdit.text()

        if "https://elenta.lt/" in url:         
            options = Options()
            options.add_argument('--incognito')
            # options.add_argument('--headless')
            driver = webdriver.Chrome(options)
            driver.get(url)     
             #Patikrinama ar https tinkamas, kitu atveju žinutė, tai pat sukuriamas csv failas ir surenkama kategorija, bei skelbimų skaičius.
            total_amount = 0
            with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Price'])
                source = driver.page_source
                html = BeautifulSoup(source, "html.parser")

                category = html.select_one("span[itemprop='itemListElement'] > span[itemprop='name']")
                category = category.text.strip().replace("»", "")
                #Paimama paieškos kategorija

                number = html.select_one(".counter")
                number = number.text.strip()
                #Paimamas skelbimų skaičius

                while True:
                #Loopas kuris eina per puslapius, jo viduje surenkama informacija t.y. pavadinimas, kaina ir išsaugoma csv faile, taip pat sumuojamos kainos, patikrrinamas ar 'sekantis' mygtukas/ elementas egzistuoja jeigu egzistuoja paspaudžiamas. 
                    agree_button = driver.find_elements(By.CSS_SELECTOR, '.fc-button-label')
                    if agree_button:
                        agree_button[0].click()

                    
                    for box in html.select(".units-list li"):
                        if box:    
                            #Surenkamas pavadinimas ir kaina
                            title = box.select_one(".ad-hyperlink")
                            title = title.text.strip() if title else "Nenurodyta"

                            price = box.select_one(".price-box")
                            price = price.text.strip() if price else "0"

                            #Duomenys išsaugomi faile
                            writer.writerow([title, price])
                            #Išvalomas price selektorius nuo nereikalingų simbolių ir susumuojamas.
                            price = price.replace("€", "").replace(" ", "")
                            total_amount += int(price)
                            
                    #spaudžiamas 'sekantis' mygtukas/ elementas
                    next_button = driver.find_elements(By.CSS_SELECTOR, 'li.pagerNextPage')
                    if next_button:
                        next_button[0].click()
                        source = driver.page_source
                        html = BeautifulSoup(source, "html.parser")     
                        sleep(1)
                    else:
                        break      
            #uždaromas web puslapis ir informacija rodoma UI label skiltelyje.
            driver.quit()
            self.ui.feedback_label.setText(f"Kategorijoje:\n{category} yra {number} skelbimai/as\nBendra kainų suma yra {str(total_amount)}€")

        #rodoma žinutė jeigu url netinkamas
        else:
            self.ui.feedback_label.setText(f"{url} netinkamas web puslapis\nurrl turi priklausyti elenta.lt") 
 

 #inicijuojama programa
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.setWindowTitle("Vobalis' Final Project")
    window.show()
    app.exec()


    