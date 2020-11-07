from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

### https://shobiddak.com/cars/647396
browser = webdriver.Chrome(ChromeDriverManager().install())

# The first car was add to the Website is --> https://shobiddak.com/cars/432300



Link = "https://shobiddak.com/cars/"
CarNum = 432300

print("-------------------------------")

for iii in range(432300,667367):
    try:
        StrNumCar = str(iii)
        FinalLink = Link + StrNumCar
        browser.get(FinalLink)
        Color = browser.find_element_by_css_selector(".list_ads .list-row:nth-of-type(1) td:last-child")
        Fuel_type = browser.find_element_by_css_selector(".list_ads .list-row:nth-of-type(2) td:last-child")
        Gear_type = browser.find_element_by_css_selector(".list_ads .list-row:nth-of-type(5) td:last-child")
        engine_power = browser.find_element_by_css_selector(".list_ads .list-row:nth-of-type(7) td:last-child")
        distance = browser.find_element_by_css_selector(".list_ads .list-row:nth-of-type(8) td:last-child")
        priceCar = browser.find_element_by_class_name("post-price").text
        name = browser.find_element_by_class_name("section_title")
        Produce_Year = browser.find_element_by_class_name("section_title:last-child").text
        ## To Split the Number from whole string (price)
        price = [int(i) for i in priceCar.split() if i.isdigit()]
        listToStrPrice = ' '.join([str(elem) for elem in price])
        # To Split the Number from whole string (Produce year)
        res = [int(i) for i in Produce_Year.split() if i.isdigit()]
        listToStrYear = ' '.join([str(elem) for elem in res])
        print("The Information for these Car is : ")
        print("Name of car is ---> ",name.get_attribute('innerHTML'))
        print("The year of produce is --> ",listToStrYear)
        print("its Color is --->",Color.get_attribute('innerHTML'))
        print("Fuel type is --->",Fuel_type.get_attribute('innerHTML'))
        print("Gear type is --->",Gear_type.get_attribute('innerHTML'))
        print("engine power is --->",engine_power.get_attribute('innerHTML'))
        print("The amount of use the car in km--->",distance.get_attribute('innerHTML'))
        print("The price for This car is -->",listToStrPrice)
        print("------------------------------------")
        # browser.quit()
        # iii = iii + 1
    except:
        iii = iii + 1


