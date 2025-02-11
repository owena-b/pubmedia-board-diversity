# Public media board diversity
**Data by Owen Auston-Babcock for [Current](https://current.org/). Story by Tyler Falk and Owen Auston-Babcock**

================
* [Overview](#overview)
* [Data](#data)
* [Methodology](#methodology)
  * [How we analyzed ownership reports](#how-we-analyzed-ownership-reports)
  * [How we analyzed Census data](#how-we-analyzed-census-data)
  * [What's in here?](#whats-in-here)
* [Limitations](#limitations)
* [License](#license)

## Overview
*[Back to top](#public-media-board-diversity)*

Most governing boards in the U.S. public media system fail to represent the racial and ethnic diversity of their communities,
undercutting the system's mission to reflect the people it intends to serve, according to an analysis of FCC and Census
Bureau data by Current, the news source for people in public media.

Read the story: [Analysis of public media boards shows lack of racial diversity](https://current.org/<insert story>) by Tyler 
Falk and Owen Auston-Babcock. Owen Auston-Babcock wrote the code contained in this repository and analyzed the data for 
this story.

## Data
*[Back to top](#public-media-board-diversity)*

We analyzed the data collected by scripts in this repository in a [Google Sheets file](https://docs.google.com/spreadsheets/d/1ej5esVtmqLXqRsy53mqockGRxzLd78jiUca_CHZBaKI/edit?usp=sharing).

## Methodology
*[Back to top](#public-media-board-diversity)*

### How we analyzed ownership reports

*See [What's in here?](#whats-in-here) for explanation of each file in this repository.*

This analysis of the system's boards relies on data we scraped from the FCC's Licensing and Management System. Stations,
which are licensed by the FCC, publish biennial (once every other year) reports on ownership and management.

We first created a list of public broadcasters who receive the Community Service Grant from the Corporation for Public
Broadcasting, then manually retrieved links to each recipient's most recent biennial report. We whittled down the
original CPB list of 547 by filtering out school districts, colleges, universities and tribal entities because the 
duty of these licensees' governing boards is not primarily the operations of a public media station. Therefore, our 
analysis is limited to stations whose governing boards are responsible for overseeing the broadcaster, and have no
other primary function. 

We used the new list to retrieve the biennial reports which are conveniently published as tables on the LMS's website, 
and created a list of board members, storing information on each member such as their occupation, gender, race and
ethnicity.

### How we analyzed Census data
*[Back to top](#public-media-board-diversity)*



### What's in here?
*[Back to top](#public-media-board-diversity)*

This project contains the following folders and files:
* `call-letters` -- 
  * `call-letters.csv` -- 
  * `call-letters-scraper.py` -- 
* `census` -- 
  * `acs-requests.py` -- 
  * `census-gets.py` -- 
  * `cities_of_license.csv` -- 
  * `city_demos.csv` -- 
  * `city_demos2.csv` -- 
  * `fips-codes.py` -- 
  * `licensee_locs.csv` -- 
  * `licensee_locs2.csv` -- 
  * `test.csv` -- 
  * `us_places_fips.csv` -- 
* `src-scrape` -- 
  * `board-scraper.py` -- 
  * `date-scraper.py` -- 
  * `dates.csv` -- 
  * `dates.py` -- 
  * `fixes.py` -- 
  * `Grantee_Ownership_Report_Links.csv` -- 
  * `pubmedia-board-members-data.csv` -- 

## Limitations
*[Back to top](#public-media-board-diversity)*


## License

**Credit:**
[JeffPaine on GitHub](https://gist.github.com/JeffPaine/3083347) for a simple Python dictionary that translates state postal abbreviations into their full common names.
