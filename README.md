                    README:

This script scrapes tweets for given Twitter handles and saves them to separate CSV files. The Twitter handles and individual terms to search for are read from files "ABC.txt" and "XYZ.txt" respectively.

Installation
The following libraries need to be installed to run the script:

pandas
numpy
selenium
snscrape
Usage
Replace the path in line 43 to the folder where you want to save the CSV files.
Update the file "ABC.txt" with the Twitter handles you want to scrape tweets for.
Update the file "XYZ.txt" with the individual terms you want to search for in the tweets.
Run the script.
The script will scrape tweets for each Twitter handle in the "ABC.txt" file and save them to separate CSV files named after the respective handles. The tweets will be searched for the individual terms in the "XYZ.txt" file, starting from the date specified in the since parameter. The combined pandas DataFrame of all the scraped tweets is returned by the get_tweets() function.

The script is compatible with Python 3.6+.# WebScraper
