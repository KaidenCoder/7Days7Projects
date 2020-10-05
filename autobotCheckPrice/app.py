from bs4 import BeautifulSoup
import requests
import smtplib

URL = 'https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JWZQJB/ref=sr_1_1_sspa?crid=2GM1N7J8BS113&dchild=1&keywords=macbook+pro&qid=1601911746&sprefix=macb%2Caps%2C324&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySU4zQUFQMVBXVFY1JmVuY3J5cHRlZElkPUEwNDI4NzUwM1Y3RUxESExKSU4wRCZlbmNyeXB0ZWRBZElkPUEwODMyMDA1M1RPNEk1NkNZRkRQSCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    s = price.replace(',', '')
    converted_price = float(s[2:10])

    # if(converted_price < 150000):
    #     send_email()

    print(converted_price)
    print(title.strip())
    if(converted_price > 150000):
        send_email()


useremail = ''
password = ''

receiveremail = ''


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # server.ehlo()

    server.login(useremail, password)

    subject = 'Do not worry!'
    body = 'Check the amazon link https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JWZQJB/ref=sr_1_1_sspa?crid=2GM1N7J8BS113&dchild=1&keywords=macbook+pro&qid=1601911746&sprefix=macb%2Caps%2C324&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySU4zQUFQMVBXVFY1JmVuY3J5cHRlZElkPUEwNDI4NzUwM1Y3RUxESExKSU4wRCZlbmNyeXB0ZWRBZElkPUEwODMyMDA1M1RPNEk1NkNZRkRQSCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        useremail,
        receiveremail,
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')
    server.quit()


check_price()
