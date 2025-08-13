from selenium import webdriver
from bs4 import BeautifulSoup
import time
url = 'https://www.resumeviking.com/templates/'
driver = webdriver.Chrome()
driver.get(url)
with open('resume_templates.txt', 'w') as file:
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        template_sections = soup.find_all('div', class_='card-template')

        for section in template_sections:
            templates = section.find_all('div', class_='card-template__download')
            for template in templates:
                links = template.find_all('a')
                for link in links:
                    link_text = link.get_text(strip=True)
                    link_href = link.get('href')
                    if link_text == "pdf":
                        file.write(f'{link_href}\n')

        try:
            next_button = driver.find_element_by_css_selector('.pagination-next')  
            next_button.click()
            time.sleep(2)  
        except:
            break  
driver.quit()
