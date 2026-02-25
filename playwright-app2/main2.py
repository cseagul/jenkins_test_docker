from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://mishpacha.com/")
        print(f"Page Title: {page.title()}")
        page.screenshot(path="screenshots/example.png")
        browser.close()

if __name__ == "__main__":
    run()