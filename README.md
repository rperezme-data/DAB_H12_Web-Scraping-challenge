# H12_Web-Scraping-challenge
## Web App: Scrape data from various websites & Display in a single HTML page

### Description
The scope of this project is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.


### Script Summary
The web application was built using Python, Flask, Jinja, HTML & Bootstrap. Data scraping was carried out using Beautiful Soup, Pandas and Splinter and a NoSQL Database (MongoDB) was used to store and retrieve data with PyMongo. 


### Workflow

#### 1. Scraping (Beautiful Soup, Pandas & Splinter)

  + **Nasa Mars News**: Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text.

  + **JPL Mars Space Images - Featured Image**: Visit the url for the [Featured Spage Image](https://spaceimages-mars.com/) site and Navigate the site and get image url for the current Featured Mars Image.

  + **Mars Facts**: Visit the [Mars Facts](https://galaxyfacts-mars.com/) webpage and use scrape the *Mars-Earth Comparison* table. 

  + **Mars Hemispheres**: Visit and Navigate the [Astrogeology](https://marshemispheres.com/) site to retrieve high resolution images url and the Hemisphere Title.

  The scraping code was enclosed in a Python script (*scrape function*) that returns one Python dictionary containing all of the scraped data.
  
#### 2. Web Application (Flask, Jinja & MongoDB)

Flask framework was used to define two routes:

  + **Homepage route `\`** that queries MongoDB and passes Mars data into a rendered HTML template to display previously scraped and stored data. Jinja was used to load data from the variable passed by Flask.


  + **Scrape route `\scrape`** that Executes the *scrape function* to scrape websites and retrieve current data, Stores the returned values in MongoDB & Redirects to Homepage.

A template file called `index.html` was created using Bootstrap in order to display all of the data in the appropiate HTML elements and structure. Database CRUD applications were performed with PyMongo. Jinja was used to load data (from the variable passed by Flask) into the rendered template.


### Screenshot
![WebApp_Screenshot](MissionToMars/Images/WebApp_Screenshot.png)
