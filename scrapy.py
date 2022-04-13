from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import dataframe_image as dfi
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
    
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    
    time.sleep(1)
    
    html = browser.html
    soup2 = bs(html, "html.parser")
    
    main_image = "https://spaceimages-mars.com/"+soup2.find_all('a', class_="showimg fancybox-thumbs")[0]['href']
    
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    
    time.sleep(1)
    
    html = browser.html
    soup3 = bs(html, "html.parser")
    
    file_path = soup3.find("table", class_="table table-striped")
    file_path
    
    milist = {
        "sloth": news_title,
        "frolick": news_p,
        "sleuth": main_image,
        "knight": file_path
    }
    
    browser.quit()
    return milist