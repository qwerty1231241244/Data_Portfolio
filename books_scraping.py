from playwright.sync_api import sync_playwright
import pandas as pd

data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")

    for _ in range(50):
        books = page.locator(".product_pod")
        for book in books.all():
            title = book.locator("h3 a").get_attribute("title")
            price = float(book.locator(".price_color").text_content().replace("£", ""))
            data.append({"product": title, "price": price, "category": "Book"})

        next_btn = page.locator(".next a")
        if next_btn.count() > 0:
            next_btn.click()
            page.wait_for_selector(".product_pod")
        else:
            break

    browser.close()

df = pd.DataFrame(data)
df["discounted_price"] = df["price"] * 0.9
df.to_excel("books_scraping.xlsx", index=False)