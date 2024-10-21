
# Twitter Bot Using Selenium

This project is a simple Twitter bot that automates the process of logging into Twitter (X) and posting tweets using Python and Selenium. The bot navigates the Twitter login page, signs in with provided credentials, and tweets a message specified by the user.

## Prerequisites

- Python 3.x installed on your system
- Google Chrome browser
- ChromeDriver corresponding to your Chrome version (Download from [ChromeDriver](https://chromedriver.chromium.org/downloads))
- Selenium package (`pip install selenium`)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TheCommente/Xbot.git
   cd Xbot
   ```

2. **Install dependencies**:
   Make sure you have Selenium installed. If not, install it using:
   ```bash
   pip install selenium
   ```

3. **Download and set up ChromeDriver**:
   - Check your Chrome version (go to `chrome://settings/help` in your Chrome browser).
   - Download the matching version of ChromeDriver from [here](https://chromedriver.chromium.org/downloads).
   - Place the `chromedriver.exe` in a known directory and update the script with the correct path.

## Usage

1. **Configure your credentials**:
   Open `bot.py` and update the following variables in the `__main__` section with your test account credentials:
   ```python
   username = "your_username"
   password = "your_password"
   tweet_text = "Hello, world! This is a test tweet from Selenium."
   ```

2. **Run the script**:
   Execute the script from the command line:
   ```bash
   python bot.py
   ```

3. **The bot will**:
   - Navigate to the Twitter login page.
   - Enter the provided username and password.
   - Log into the account.
   - Compose a tweet with the specified message and post it.

## Code Explanation

- **`login_to_twitter(driver, username, password)`**:
   This function automates the process of logging into Twitter using the provided credentials.
   
- **`tweet(driver, message)`**:
   This function navigates to the tweet composition page, writes the tweet, and posts it.
   
- **`WebDriverWait` and `expected_conditions`**:
   Used for waiting until certain elements are present or clickable, ensuring that the script interacts with the web page at the right time.

## Important Notes

- **Use a test account**: Do not use your primary account credentials for testing as it may lead to your account being flagged or banned.
- **Selenium Limitations**: Selenium automates web browsers by simulating user behavior, which is detectable by some websites. Twitter may restrict actions performed by automated bots.
- **ChromeDriver Version**: Make sure the ChromeDriver version matches your installed Chrome browser version. If not, download the correct version from [here](https://chromedriver.chromium.org/downloads).

## Troubleshooting

1. **Timeout Exceptions**:
   - If the bot is unable to find certain elements, the page may have changed, or elements are taking too long to load. Try increasing the wait time in the `WebDriverWait` calls.

2. **ChromeDriver Errors**:
   - Ensure that the `chromedriver.exe` path is correct and that the version matches your installed Chrome version.

3. **Two-Factor Authentication**:
   - The script does not support 2FA. Disable 2FA for the test account or use an account without 2FA.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is intended for educational purposes only. The use of automated scripts on websites like Twitter is against their Terms of Service. Use this script at your own risk.
