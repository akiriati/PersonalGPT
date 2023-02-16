# from playwright.sync_api import sync_playwright
#
#
# class PlaywrightScrapper():
#
#     def get_html(self, url):
#         with sync_playwright() as playwright:
#             browser = playwright.chromium.launch()
#             page = browser.newPage()
#             page.goto(url)
#             text_content = page.evaluate("document.body.textContent")
#             browser.close()
#             return text_content


