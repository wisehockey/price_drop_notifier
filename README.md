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