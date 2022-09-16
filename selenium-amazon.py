from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10) #if something not available imediately then it will wait for 10 sec

driver.find_element(By.XPATH, "//input[contains(@id,'twotabsearchtextbox')]").send_keys('redmi note 5 pro')
driver.find_element(By.XPATH,"//input[contains(@id,'nav-search-submit-button')]").click()
driver.find_element(By.XPATH,"//span[text()='Redmi']").click()


file1 = open('myfile.txt', 'w+')
try:
    while True:
        phone_names = driver.find_elements(By.XPATH,"//span[contains(@class,'a-size-medium a-color-base a-text-normal')]")
        phone_price = driver.find_elements(By.XPATH,"//span[contains(@class,'a-price-whole')]")
        
        for phone in phone_names:
            file1.write(phone.text+"\n\n")
        next_button = driver.find_element(By.XPATH,"//a[contains(@class,'s-pagination-item s-pagination-next s-pagination-button s-pagination-separator')]")
        next_button.click()
except Exception:
    file1.close()
    print("Data is written in file.")
