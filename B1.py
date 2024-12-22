from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 设置Chrome选项以在必要时启用无头模式或其他选项
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 无头模式，浏览器不会弹出界面

# 指定Chrome驱动的位置
webdriver_service = Service(r'E:\chromedriver-win64\chromedriver.exe')

# 初始化WebDriver
# driver = webdriver.Chrome(service=webdriver_service,options=chrome_options)
driver = webdriver.Chrome("E:\chromedriver-win64\chromedriver.exe",options=chrome_options)

# 打开百度首页
driver.get("https://www.baidu.com")

# 找到搜索框元素
search_box = driver.find_element(By.ID, "kw")

# 输入搜索关键词
search_box.send_keys("Selenium")

# 找到搜索按钮元素并点击
search_button = driver.find_element(By.ID, "su")
search_button.click()

# 等待页面加载完成，这里等待5秒
time.sleep(5)

# 关闭浏览器
driver.quit()

