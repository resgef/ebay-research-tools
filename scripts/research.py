#!/usr/bin/env python
import requests

endpoint = 'http://svcs.ebay.com/services/search/FindingService/v1'
headers = {
    'X-EBAY-SOA-SECURITY-APPNAME': 'SAMPLE-paulsl-PRD-02466ad0e-95ff6e2e',
    'X-EBAY-SOA-OPERATION-NAME': 'findItemsByKeywords',
    'X-EBAY-SOA-GLOBAL-ID': 'EBAY-US',
    'X-EBAY-SOA-RESPONSE-DATA-FORMAT': 'json'
}
xml = """
 <?xml version="1.0" encoding="UTF-8"?>
<findItemsByKeywordsRequest xmlns="http://www.ebay.com/marketplace/search/v1/services">
  <keywords>harry potter phoenix</keywords>
  <paginationInput>
    <entriesPerPage>100</entriesPerPage>
  </paginationInput>
</findItemsByKeywordsRequest>
 """

r = requests.get("""
http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=SAMPLE-paulsl-PRD-02466ad0e-95ff6e2e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=harry%20potter%20phoenix&paginationInput.entriesPerPage=100
""")

resp_json = r.content
total_listed = resp_json['findItemsByKeywordsResponse']['paginationOutput'][0]['totalEntries']

with open('./output.json', 'w') as f:
    f.write(r.content.decode('utf-8'))
    f.close()
