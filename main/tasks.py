import re
import time

from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .models import ScrapedData


@shared_task
def extract_emails(url, scraped_data_id):
    try:
        scraped_data = ScrapedData.objects.get(id=scraped_data_id)
        scraped_data.status = ScrapedData.Status.IN_PROGRESS
        scraped_data.save()

        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode

        # Set up the Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the URL
        driver.get(url)

        # Wait for the page to load (you might need to adjust this time)
        time.sleep(5)

        # Get the page source after JavaScript has rendered the content
        content = driver.page_source

        # Close the browser
        driver.quit()

        # Use regex to find all email addresses
        email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        emails = re.findall(email_pattern, content)

        # save the emails to the database
        scraped_data = ScrapedData.objects.get(id=scraped_data_id)
        scraped_data.data = ', '.join(set(emails))
        scraped_data.status = ScrapedData.Status.SUCCESS
        scraped_data.save()

        # Remove duplicates and return the list
        return ', '.join(set(emails))

    except Exception as e:
        print(f"An error occurred: {e}")

        # Return can't extract emails
        scraped_data = ScrapedData.objects.get(id=scraped_data_id)
        scraped_data.status = ScrapedData.Status.FAILED
        scraped_data.description = "Can't extract emails"
        scraped_data.save()
        return []
