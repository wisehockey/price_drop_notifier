import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

# Set up Twilio
twilio_account_sid = 'TWILIO_ACCOUNT_SID'
twilio_auth_token = 'TWILIO_AUTH_TOKEN'
twilio_whatsapp_number = 'TWILIO_WHATSAPP_NUMBER'  # Your Twilio WhatsApp sandbox number
your_whatsapp_number = 'YOUR_WHATSAPP_NUMBER'  # Your personal WhatsApp number

# Twilio client setup
client = Client(twilio_account_sid, twilio_auth_token)

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument('--headless')

# Use Service to manage the ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

previous_price = None

def send_whatsapp_message(message):
    """Function to send WhatsApp message using Twilio"""
    client.messages.create(
        body=message,
        from_=twilio_whatsapp_number,
        to=your_whatsapp_number
    )

def scrape_interval():
    global previous_price
    while True:
        time.sleep(60)  # Wait for 1 minute before scraping again
        
        driver.get("target_url")
        
        try:
            # Extract the price from the page
            price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
            current_price = float(price_element.text.replace(",", ""))  # Convert to float for comparison
            
            print(f"Current Price: ${current_price}")
            
            if previous_price is None:
                previous_price = current_price  # Initialize the previous price
            elif current_price < previous_price:
                # If the price has decreased, send a WhatsApp message
                message = f"Price Alert: The price of the product has decreased! New price: ${current_price}"
                send_whatsapp_message(message)
                print("Price decreased, message sent.")
                
                # Update the previous price to the new price
                previous_price = current_price

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)  # Scrape every minute to check the price again

# Start scraping the product's price
scrape_interval()
