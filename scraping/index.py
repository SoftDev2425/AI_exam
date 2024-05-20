from link_scraper import scrape_links
from house_data_scraper import house_data_scrape
from selenium import webdriver
from accept_terms import accept_terms
import time

def scrape_data_for_zipcodes(zipcodes, browser):
    for zipcode in zipcodes:
        print(f"Scraping data for zip code: {zipcode}")
        try:
            scrape_links(zipcode, browser)
            house_data_scrape(zipcode, browser)
            print(f"Data for zip code {zipcode} has been scraped.")
        except Exception as e:
            print(f"Error scraping data for zip code {zipcode}: {e}")

if __name__ == "__main__":
    
    browser = webdriver.Firefox()
    browser.get('https://www.dingeo.dk')
    time.sleep(2)
    
    accept_terms(browser)

    #zipcodes = [3220,3210,3250,3120,3230,3200, 3100,3140,3150,3000,3070,3060,3490,3080,3490,3050,2990,2980,3480,3320,3400,3330,3450,3540,3550,3600,2970,2960,2950,3460,2840,2850,2942,3650,3660,3670,2765,2760,2750,2740,2830,2800,2930,2880,2860,2820,2920,2900,2870, 2620, 2600,2610,2720,2700, 2400, 2100, 2150, 2300,2450, 2690, 2640,2630, 2500, 2450, 2770, 2791,1432, 2650, 3300, 3310, 3360, 3370, 4000]
    zipcodes = [
        3220, 
        2620
    ]
    unique_zipcodes = set(zipcodes)
    sorted_zipcodes = sorted(unique_zipcodes)
    try:
        scrape_data_for_zipcodes(sorted_zipcodes, browser)
    finally:
        browser.quit()
