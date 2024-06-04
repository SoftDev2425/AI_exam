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

    zipcodes = [2100,2620,2740,2750,2760,2950,2960,2970,2980,2990,3000,3050,3060,3070,3080,3100,3120,3140,3150,3200,3210,3220,3230,3250,3320,3480,3490,2300,2400,2450,2500,2600,2610,2630,2640,2650,2690,2700,2720,2765,2770,2791,2800,2820,2830,2840,2850,2860,2870,2880,2900,2920,2930,2942,3300,3310,3360,3370,3400,3450,3460,3540,3550,3600,3650,3660,3670,4000
               ]
    
    unique_zipcodes = set(zipcodes)
    sorted_zipcodes = sorted(unique_zipcodes)
    try:
        scrape_data_for_zipcodes(sorted_zipcodes, browser)
    finally:
        browser.quit()
