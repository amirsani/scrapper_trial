import json
import sys
import urllib.parse
link = urllib.parse.unquote(sys.argv[1])
from playwright.sync_api import sync_playwright
print(link)
with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36')
    page = context.new_page()
    page.goto(link)
    try:
        page.wait_for_timeout(10000)
        print(page.content())
        page.close()
        context.close()
        browser.close()      
    except Exception as e:
        print("Error in playwright script.")
        page.close()
        context.close()
        browser.close()