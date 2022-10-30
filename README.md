# Burner

Easy to use script to determine the cheapest price for [SimSMS](https://simsms.org/).

I've provided a database with price information. If you'd like to create your own,
you'll have to make your own API key on your SimSMS profile page and use the
`--authorization` option. You will also need to delete the `sms.db` file if it exists
before doing this.

## Installation

1. Clone the repository.
2. `pip install -r requirements.txt`

## Usage

Use the following command to find the code for the service you want.

```bash
py sms.py services
```

Then use the following command to find the price list for the service.

```bash
py sms.py prices opt29 # This will get the price list for Telegram.
```
