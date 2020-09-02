# Project 2
Tri-County Health Department Restaurant Inspections

# Data Source
https://data.colorado.gov/Health/Restaurant-Inspections-in-Tri-County-Colorado/869n-zj3f

After taking a exceptionally long time to look for a dataset that made sense, I landed on the "Restaurant Inspections in Tri-County Colorado".
This dataset popped out to me because it (literally) hits close to home and it piqued my curiousity to know how restaurants scored on the ratings.


# Dataset
The dataset contains 5,555 records of restaurant inspections in the Adams-Arapahoe-Douglas county area of Colorado. It shows detailed accounts of when, 
where and how the inspections were conducted; the name, address and latitude/longitude of the restaurant locations; and, a record of each restaurant's 
performance of the 56 violations tracked by the health department. (1 = Violated, 0 = Not violated).

# Outline
Since I am constricted by time, I was not able to fully prepare what I had in mind for this project. So I hope to explain my thought process best in an
outline.

* Python/SQLite/100+ Records
  * Open/Read the CSV file in Jupyter notebook using pandas.
  * Filter and visualize the data using pandas and matplotlib.
  * Take comparison data and connect to an SQLite server.

* HTML/CSS/Interaction/Javascript/D3/JSlibrary
  * Implement a custom HTML/CSS style that would allow for drop down menu interactions, a functioning search box, and a Google Maps API search area.
  * Import data from SQLite using a Flask API.
  * Use the imported data to create D3 Visualizations using Javascript. Would be displayed on a "data.html" webpage.
  
* Other: Anime.js and Tableau
  * Would use anime.js library for creative, fun looking loading screens when transitioning (shown on app.js)
  * Would search for additional visuals in Tableau if necessary.

# Observations
Some of the relationships in the data I wanted to explore include and are not limited to:
* Group by Restaurant size and Risk factor
* Group by county and city
* Freq of infractions (overall and by each category)
* How to potentially call to another database that can act as a verification of these checks (CDPHE Database).
* Create a couple of extra columns to reflect an overall Inspection score which can be used as a rating system for these restaurants.

* I wanted to take advantage of the Latitude/Longitude data provided in the dataset and use it for a Google search area that would be a part of my ultimate search tool.
* I wanted to implement drop down bars where you can go to webpages that have individual dashboards for each restaurant, you can examine results per county.
* *THE BIGGEST* thing I wanted to create was a search tool. It'd be a rectangular box on the webpage consisting of four fields to search for a restaurant in your area,
  when the search is complete, Google Maps box would display the restaurant(s) in the area and also display their risk factor by color (red, yellow or green). Furthermore,
  if you clicked on a particular restaurant, information would be displayed below the Google Map area and provide Restaurant name, address, Inspection Score and Risk factor.
  (REFER TO IMAGES FOLDER FOR VISUAL).
  
I **really really** wish I had more time to examine this dataset for the bootcamp because I believe I was on the verge of creating a hybrid visual spectacle and handy search
tool. After boocamp is over, I plan on coming back to this to create a final product. This project was incredibly fun even in this short amount of time. Will hope to provide
updates in subsequent READMEs. 
