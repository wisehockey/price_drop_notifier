# Amazon Price Drop Notifier

This script tracks price drops for a product on Amazon and sends a WhatsApp alert via Twilio.

## Features
- Scrapes the price of a product at a set interval.
- Sends a WhatsApp message if the price drops.
- Uses environment variables for secure credential handling.

## Requirements
- Python 3.x
- Twilio account with WhatsApp sandbox access
- Google Chrome & ChromeDriver

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/amazon-price-drop-notifier.git
   cd amazon-price-drop-notifier

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Update Twilio Credentials.

## How to Use

1. Ensure Chrome and ChromeDriver are installed

   ChromeDriver is automatically managed by webdriver-manager, so no manual installation is needed.

2. Verify Twilio Setup

   Sign up at Twilio.

   Activate the Whatsapp sandbox and verify your phone number.

3. Modify Product URL

    ```bash
    driver.get("https://www.amazon.in/your-product-link")

4. Stop the script when you are done

   The script runs indefinitely. To stop it, press Ctrl + C