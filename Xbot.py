from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_to_twitter(driver, username, password):
    driver.get("https://x.com/i/flow/login")
    
    # Wait for the username input to be present and then enter the username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "text")))
    username_input = driver.find_element(By.NAME, "text")
    username_input.send_keys(username)

    # Wait for the "Next" button to be clickable and then click it
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next' or text()='הבא']"))
    )
    next_button.click()

    # Wait for the password input to be present and then enter the password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(password)

    # Wait for the "Log in" button to be clickable and then click it
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in' or text()='כניסה']"))
    )
    login_button.click()

    # Optional: wait for a few seconds after logging in
    time.sleep(5)

def tweet(driver, message):
    driver.get("https://twitter.com/compose/tweet")
    
    # Wait for the tweet box to be present and then enter the tweet
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "public-DraftStyleDefault-block")))
    tweet_box = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
    tweet_box.send_keys(message)

    # Wait for the "Post" button to be clickable and then click it
    post_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='tweetButton']"))
    )
    post_button.click()

    # Optional: wait for a few seconds to make sure the tweet is posted
    time.sleep(3)


if __name__ == "__main__":
    username = "YourUsername" # your twitter username
    password = "YourPassword" # your twitter password
    tweet_text = "Test Passed successfully!" # the tweet text

    # Create a Service instance for ChromeDriver
    service = Service("Your\\chromedriver.exe\\path") # path to your chromedriver.exe
    # C:\\chromedriver-win32\\chromedriver.exe
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_to_twitter(driver, username, password)
        tweet(driver, tweet_text)
        print("Tweeted successfully!")
    finally:
        driver.quit()
