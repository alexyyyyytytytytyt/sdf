from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager



def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    
    url="https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title = soup.find_all("div", class_="content_title")[0].text
    news_p = soup.find_all("div", class_="article_teaser_body")[0].text

    malist = {
        "sloth" : news_title,
        "frolick" : news_p
    }
    
    browser.quit()

    return malist