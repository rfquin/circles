"""
Program extracts raw data for Programs and place data in file
'programsRaw.json', ready for formatting.

Step in the data's journey:
    [ X ] Scrape raw data (programScraper.py)
    [   ] Format scraped data (programFormatting.py)
    [   ] Customise formatted data (programProcessing.py)
"""
from datetime import date
import requests
import json
import ast
import data.utility.dataHelpers

THIS_YEAR = str(date.today().year) # Ensures request remains up-to-date
TOTAL_PGRMS = 249 # Update if number of programs increases

PAYLOAD = {
    "query": {
        "bool": {
            "must": [{
                    "term": {
                        "live": True
                    }
                },
                [{
                    "bool": {
                        "minimum_should_match": "100%",
                        "should": [{
                            "query_string": {
                                "fields": ["unsw_pcourse.studyLevelValue"],
                                "query": "*ugrd*"
                            }
                        }]
                    }
                }, {
                    "bool": {
                        "minimum_should_match": "100%",
                        "should": [{
                            "query_string": {
                                "fields": ["unsw_pcourse.implementationYear"],
                                "query":f"*{THIS_YEAR}*"
                            }
                        }]
                    }
                }, {
                    "bool": {
                        "minimum_should_match": "100%",
                        "should": [{
                            "query_string": {
                                "fields": ["unsw_pcourse.active"],
                                "query": "*1*"
                            }
                        }]
                    }
                }]
            ],
            "filter": [{
                "terms": {
                    "contenttype": ["unsw_pcourse", "unsw_pcourse"]
                }
            }]
        }
    },
    "sort": [{
        "unsw_pcourse.code_dotraw": {
            "order": "asc"
        }
    }],
    "from": 0,
    "size": 249,
    "track_scores": True,
    "_source": {
        "includes": ["*.code", "*.name", "*.award_titles", "*.keywords", "urlmap", "contenttype"],
        "excludes": ["", None]
    }
}


'''
Retrieves data for all undergraduate programs 
'''
def scrape_programs():
    url = "https://www.handbook.unsw.edu.au/api/es/search"
    headers = {
        "content-type": "application/json",
    }
    r = requests.post(url, data=json.dumps(PAYLOAD), headers=headers)
    dataHelpers.write_data(r.json()["contentlets"], 'programsRaw.json')


if __name__ == "__main__":
    scrape_programs()
    
