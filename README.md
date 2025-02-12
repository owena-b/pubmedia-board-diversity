# Public media board diversity

================
* [Overview](#overview)
* [Data](#data)
* [Methodology](#methodology)
  * [How we analyzed ownership reports](#how-we-analyzed-ownership-reports)
  * [How we analyzed Census data](#how-we-analyzed-census-data)
  * [What's in here?](#whats-in-here)
* [Limitations & Assumptions](#limitations--assumptions)
* [Credit](#credit)

## Overview
*[Back to top](#public-media-board-diversity)*

Most governing boards in the U.S. public media system fail to represent the racial and ethnic diversity of their
communities, undercutting the system's mission to reflect the people it intends to serve, according to an analysis of
FCC and Census Bureau data by [Current, the news source for people in public media](https://current.org/).

Read the story: [Analysis of public media boards shows lack of racial diversity]() by
Tyler Falk with Owen Auston-Babcock. Auston-Babcock wrote the code contained in this repository and analyzed the
data for this story.

## Data
*[Back to top](#public-media-board-diversity)*

We analyzed the data collected by scripts in this repository in a [Google Sheets file](https://docs.google.com/spreadsheets/d/1ej5esVtmqLXqRsy53mqockGRxzLd78jiUca_CHZBaKI/edit?usp=sharing).

## Methodology
*[Back to top](#public-media-board-diversity)*

*See [What's in here?](#whats-in-here) for explanation of each file in this repository.*

### How we analyzed ownership reports
*[Back to top](#public-media-board-diversity)*

This analysis of the system's boards relies on data we scraped from the FCC's Licensing and Management System. Stations,
which are licensed by the FCC, publish biennial (once every other year) reports on ownership and management.

We first created a list of public broadcasters who receive the Community Service Grant from the Corporation for Public
Broadcasting, then manually retrieved links to each recipient's most recent biennial report. We whittled down the
original CPB list of 547 by filtering out school districts, colleges, universities and tribal entities because the 
duty of these licensees' governing boards is not primarily the operations of a public media station. Therefore, our 
analysis is limited to stations whose governing boards are responsible for overseeing the broadcaster, and have no
other primary function. 

We used the new list to retrieve the biennial reports, which are conveniently published as tables on the LMS's website, 
and created a list of board members, storing information on each member such as their occupation, gender, race and
ethnicity.

### How we analyzed Census data
*[Back to top](#public-media-board-diversity)*

After collecting ownership reports and, subsequently, data on each individual board member across the system, we asked,
"Does location affect a board's diversity, and can we determine which boards represent their coverage areas well?"

We started by generating a list of all the cities and states of license for the licensees included in our analysis. We
then matched political geographies (domestic names) to statistical geographies by searching the U.S. Geological Survey's 
[Geographical Names Information System](https://www.usgs.gov/tools/geographic-names-information-system-gnis) (GNIS). We 
made a list of the standardized geographic codes associated with the places of interest. These codes are called InterNational 
Committee for Information Technology Standards (INCITS) codes, formerly known as Federal Information Processing 
Series (FIPS) codes (we primarily call it FIPS, but use INCITS and FIPS interchangeably). GNIS has its own codes, but
FIPS was compatible with the `census` Python package.

Once the list containing FIPS codes was made, we used `census` to interface with the Census Bureau's API, and got
population data for our places of interest. We had to run the code twice on different inputs, since the first list did 
not include some places included in our analysis (hence, `city_demos_2.csv` and `city_fips_2.csv`).

### What's in here?
*[Back to top](#public-media-board-diversity)*

This project contains the following folders and files:
* `call-letters` — Code and files used to collect a list of call letters for stations operated by licensees in our analysis.
  * `call-letters.csv` — List of licensees, their locations and their call numbers registered with the FCC.
  * `call-letters-scraper.py` — The code to pull call numbers from the biennial ownership reports.
  * `fixes.py` — A Python dictionary to expand states' postal abbreviations to their full names.
* `census` — Code and data used to retrieve Census data for cities/states of license.
  * `census.py` — The code to get demographics for the places in our analysis from the Census Bureau.
  * `city_demos.csv` — Output from first run of `census-gets.py`, population data for places in `city-fips.csv`
  * `city_demos2.csv` — 〃, second run
  * `city-fips.csv` — List of places in our first run of `census-gets.py`
  * `city-fips_2.csv` — List of places that were left out of first run
* `src-scrape` — Code and data used to retrieve data on board members from the FCC.
  * `board-scraper.py` — The code to get data from the FCC on more than 3,000 public media board members.
  * `date-range.py` — The code to get a date range of the reports in our analysis.
  * `date-scraper.py` — The code to get a list of all the report dates in our analysis.
  * `dates.csv` — A list of all the report dates in our analysis.
  * `fixes.py` — A Python dictionary to expand states' postal abbreviations to their full names.
  * `Grantee_Ownership_Report_Links.csv` — A list of all the links to the biennial ownership reports in our analysis.
  * `pubmedia-board-members-data.csv` — Data on more than 3,000 public media board members.

## Limitations & Assumptions
*[Back to top](#public-media-board-diversity)*

Assumes board members put the same identity they would answer on the Census ... Limited to city/state of license, not
true coverage area ... Excludes stations operated by other entities, but only includes licensees w/ their own boards

## Credit

Thanks to:
* [JeffPaine on GitHub](https://gist.github.com/JeffPaine/3083347) for a simple Python dictionary that translates state postal abbreviations into their full common names.
* [News Nerdery](https://newsnerdery.org/) community members and AU data journalism professor Aarushi Sahejpal for
sharing resources and knowledge. This work attempts, as best it can, to adhere to the best practices of data journalism.
We took inspiration from NPR Visuals' [best practices](https://github.com/nprapps/bestpractices) and The Baltimore
Banner's README files, such as [this one](https://github.com/The-Baltimore-Banner/youth-gun-violence) on 2023 youth gun
violence.