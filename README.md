# Demographic makeup of public media organizations' governing boards
By Owen Auston-Babcock for [Current](current.org)

A Python program to scrape the FCC's Licensing and Management System for public media ownership records.

Using a list provided by the Corporation for Public Broadcasting of Community Service Grant recipients, I collected links to the ownership records for each recipient (which are radio and television licensees).

The list of CSG recipients was whittled down from 547 by filtering out school districts, colleges, universities, and tribal organizations. These licensees often file the station's board as their own governing board, when in reality most boards of trustees and the like are not concerned with their radio or TV station. Tribal-affiliated and Indigenous-focused licensees were also filtered out. Our analysis is concerned with the diversity of these organizations, and stations whose purpose is to cater to an underserved group will inherently have lower diversity scores.

The [links to ownership records](Grantee_Ownership_Report_Links.csv) are contained in a CSV, which is translated to a list. The program iterates over each link, running a GET request and exporting data from the records into a [CSV](pubmedia-board-members-data.csv).

Each line in the outfile is a public media organization's board member. The data can then be used to analyze broader trends across the industry.

**Credits:**

[JeffPaine on GitHub](https://gist.github.com/JeffPaine/3083347) for a simple Python dictionary that translates state postal abbreviations into their full common names.
