# Public media board diversity
**Data by Owen Auston-Babcock for [Current](current.org). Story by Tyler Falk and Owen Auston-Babcock**

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

Read the story: [Analysis of public media boards shows lack of racial diversity](current.org/<insert story>) by Tyler 
Falk and Owen Auston-Babcock. Owen Auston-Babcock wrote the code contained in this repository and analyzed the data for 
this story.

## Data
*[Back to top](#public-media-board-diversity)*



## Methodology
*[Back to top](#public-media-board-diversity)*

### How we analyzed ownership reports

*See [What's in here?]() for explanation of each file in this repository.*

This analysis of the system's boards relies on data we scraped from the FCC's Licensing and Management System. Stations,
which are licensed by the FCC, publish biennial (once every other year) reports on ownership and management. We used these
reports, which are conveniently published as tables on the LMS's website, 



Using a list provided by the Corporation for Public Broadcasting of Community Service Grant recipients, I collected links to the ownership records for each recipient (which are radio and television licensees).

The list of CSG recipients was whittled down from 547 by filtering out school districts, colleges, universities, and tribal organizations. These licensees often file the station's board as their own governing board, when in reality most boards of trustees and the like are not concerned with their radio or TV station. Tribal-affiliated and Indigenous-focused licensees were also filtered out. Our analysis is concerned with the diversity of these organizations, and stations whose purpose is to cater to an underserved group will inherently have lower diversity scores.

The [links to ownership records](src-scrape/Grantee_Ownership_Report_Links.csv) are contained in a CSV, which is translated to a list. The program iterates over each link, running a GET request and exporting data from the records into a [CSV](src-scrape/pubmedia-board-members-data.csv).

Each line in the outfile is a public media organization's board member. The data can then be used to analyze broader trends across the industry.

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
