from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import requests
import pandas as pd
import dataframe_image as dfi
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    
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
    
    
    
    milist = {
        "sloth": news_title,
        "frolick": news_p,
        "sleuth": main_image,
    }
    
    browser.quit()
    return milist

def scrape_marsFacts():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    ## Scraping Mars Facts Webpage
    url = 'https://galaxyfacts-mars.com/'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    tables_df = ((pd.read_html(url))[1]).rename(columns={0: "Attribute", 1: "Value"}).set_index('Attribute')
    html_table = (tables_df.to_html()).replace('\n', '')
    
    mars_web = {
        "mars_data": html_table
    }
    
    browser.quit()
    return mars_web

def mars_hemispheres():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    
    url4 = "https://marshemispheres.com/"
    browser.visit(url4)
    html = browser.html
    soup4 = bs(html, "html.parser")
    
    url5 = "https://marshemispheres.com/cerberus.html"
    browser.visit(url5)
    html = browser.html
    soup5 = bs(html, "html.parser")
    
    url6 = "https://marshemispheres.com/schiaparelli.html"
    browser.visit(url6)
    html = browser.html
    soup6 = bs(html, "html.parser")
    
    url7 = "https://marshemispheres.com/syrtis.html"
    browser.visit(url7)
    html = browser.html
    soup7 = bs(html, "html.parser")
    
    url8 = "https://marshemispheres.com/valles.html"
    browser.visit(url8)
    html = browser.html
    soup8 = bs(html, "html.parser")
    
    ned = []
    ned.extend((soup5.find_all("img")[4]["src"], soup6.find_all("img")[4]["src"], soup7.find_all("img")[4]["src"], soup8.find_all("img")[4]["src"]))
    
    bib = []
    for j in ned:
        bib.append(url4+j)
        
    blip = soup4.find_all("h3")[:4]
    
    fed = []
    for (i, j) in zip(blip, bib):
        print([{"title": i.text, "img_url": j}])
        fed.append({"title": i.text, "img_url": j})
        
    first = fed[0]["img_url"]
    second = fed[1]["img_url"]
    third = fed[2]["img_url"]
    fourth = fed[3]["img_url"]
    
    Cerberus = fed[0]["title"]
    Schiaparelli = fed[1]["title"]
    Syrtis_Major = fed[2]["title"]
    Valles = fed[3]["title"]
    
    
    
    paimon = {
        "first": first,
        "second": second,
        "third": third,
        "fourth": fourth,
        "Cerberus": Cerberus,
        "Schiaparelli": Schiaparelli,
        "Syrtis_Major": Syrtis_Major,
        "Valles": Valles
    }
        
    browser.quit()
    return paimon