## Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

## SCRAPE FUNCTION
def scrape_mars():

    ## Setup Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    ## SCRAPE NASA Mars News
    ## Mars News URL
    url = "https://redplanetscience.com/"

    ## Open URL in Chrome Browser
    browser.visit(url)

    ## Make Beautiful Soup
    soup = bs(browser.html, 'html.parser')

    ## Extract News Title
    news_title = soup.find("div", class_="content_title").text

    ## Extract News Paragraph
    news_paragraph = soup.find("div", class_="article_teaser_body").text


    ## SCRAPE JPL MARS SPACE IMAGES
    ## Mars Space Images URL
    url = "https://spaceimages-mars.com/"

    ## Open URL in Chrome Browser
    browser.visit(url)

    ## Make Beautiful Soup
    soup = bs(browser.html, 'html.parser')

    ## Extract image URL
    featured_image_src = soup.find("img", class_="headerimage fade-in")["src"]
    featured_image_url = url + featured_image_src

    ## SCRAPE MARS FACTS
    ## Mars Facts URL
    url = "https://galaxyfacts-mars.com/"

    ## Extract Tables from URL
    tables = pd.read_html(url)

    ## Convert "Mars Planet Profile" Table to DataFrame
    mars_facts_df = tables[1]

    ## Export table (HTML) from DataFrame
    facts_table = mars_facts_df.to_html(justify="left",
        classes="table table-responsive table-bordered table-striped",
        border=0)

    ## SCRAPE MARS HEMISPHERES
    ## Mars Hemispheres URL
    url = "https://marshemispheres.com/"

    ## Open URL in Chrome Browser
    browser.visit(url)

    ## Set variables
    hemisphere_image_urls = []

    ## Scrape Loop
    for i in range(4):

        ## Click "Hemisphere" link
        browser.links.find_by_partial_text("Hemisphere")[i].click()
        ## Click "Open" link
        browser.links.find_by_partial_text("Open").click()

        ## Make Beautiful Soup
        soup = bs(browser.html, 'html.parser')

        ## Extract hemisphere title
        title_raw = soup.find("h2", class_="title").text
        title_clean = title_raw.split(" Enhanced")[0]

        ## Extract hemisphere image url
        img_src = soup.find("img", class_="wide-image")["src"]
        img_url = url + img_src

        ## Append hemisphere title & image as {key:value}
        hemisphere_image_urls.append({"title": title_clean, "img_url": img_url})

        ## Back Chrome Browser
        browser.back()
    
    ## Close Chrome Browser
    browser.quit()

    ## Build results dictionary
    results = {'news_title': news_title,
        'news_paragraph': news_paragraph,
        'featured_image_url': featured_image_url,
        'facts_table': facts_table,
        'hemisphere_image_urls': hemisphere_image_urls}

    ## Print
    print("Scrape completed")
        
    return (results)

