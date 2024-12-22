from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Page Object Model 类
class BaiduPage:


# 初始化WebDriver和等待时间

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


# 页面元素定位器
search_box_id = 'kw'
search_button_id = 'su'


# 打开百度首页
def open_link(self):
    self.driver.get('https://www.baidu.com')


# 输入搜索关键词
def search_key(self, keyword):
    search_box = self.driver.find_element(By.ID, self.search_box_id)
    search_box.clear()
    search_box.send_keys(keyword)


# 点击搜索按钮
def click_search_button(self):
    search_button = self.driver.find_element(By.ID, self.search_button_id)
    search_button.click()


# 等待搜索结果
def wait_search_result(self):
    self.wait.until(EC.presence_of_element_located((By.ID, 'content_left')))


# 使用POM进行UI自动化测试
if __name__ == "__main__":
    # 初始化WebDriver
    driver = webdriver.Chrome()

    # 创建百度页面实例
    Baidu = BaiduPage()

    try:
        # 打开百度首页
        open_link()

        # 输入搜索关键词
        # 百度.输入搜索关键词('Python')
        search_key('Python')

        # 点击搜索按钮
        # 百度.点击搜索按钮()
        click_search_button()

        # 等待搜索结果
        # 百度.等待搜索结果()
        wait_search_result()

        # 其他测试步骤...

    finally:
        # 关闭WebDriver
        driver.quit()