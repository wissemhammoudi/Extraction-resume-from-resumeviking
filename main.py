from selenium import webdriver
from bs4 import BeautifulSoup
import time
# Define the URL
url = 'https://www.resumeviking.com/templates/'
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()
# Navigate to the URL
driver.get(url)
# Open the text file for writing
with open('resume_templates.txt', 'w') as file:
    while True:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extracting the resume templates
        template_sections = soup.find_all('div', class_='card-template')

        for section in template_sections:
            templates = section.find_all('div', class_='card-template__download')
            for template in templates:
                # Extracting download links
                links = template.find_all('a')
                for link in links:
                    link_text = link.get_text(strip=True)
                    link_href = link.get('href')
                    if link_text == "pdf":
                        file.write(f'{link_href}\n')

        # Try to find and click the 'next' pagination button
        try:
            next_button = driver.find_element_by_css_selector('.pagination-next')  # Update the selector according to the website's structure
            next_button.click()
            time.sleep(2)  # Wait for the page to load
        except:
            break  # Exit the loop if there's no next button
# Close the browser
driver.quit()
