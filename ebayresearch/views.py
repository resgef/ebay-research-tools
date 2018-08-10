from django.shortcuts import render
from .forms import SearchForm
import requests


def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        r = requests.get("""
        http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=SAMPLE-paulsl-PRD-02466ad0e-95ff6e2e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=harry%20potter%20phoenix&paginationInput.entriesPerPage=100
        """)

        resp_json = r.content
        pagination = {
            'pageNumber': resp_json['findItemsByKeywordsResponse']['paginationOutput'][0]['pageNumber'],
            'entriesPerPage': resp_json['findItemsByKeywordsResponse']['paginationOutput'][0]['entriesPerPage'],
            'totalPages': resp_json['findItemsByKeywordsResponse']['paginationOutput'][0]['totalPages'],
            'totalEntries': resp_json['findItemsByKeywordsResponse']['paginationOutput'][0]['totalEntries']

        }
        items = []
        for item in resp_json['findItemsByKeywordsResponse']['searchResult']['item']:
            items.append({
                'itemId': item['itemId'],
                'title': item['title'],
                'galleryURL': item['galleryURL'],
                'viewItemURL': item['viewItemURL'],
                'shipping_cost': 'Free' if item['shippingInfo'][0]['shippingType'] == 'Free' else
                item['shippingInfo'][0]['shippingServiceCost'][0]['@currencyId'] +
                item['shippingInfo'][0]['shippingServiceCost'][0]['__value__'],
                'price': item['sellingStatus'][0]['currentPrice'][0]['@currencyId'] +
                         item['sellingStatus'][0]['currentPrice'][0]['__value__']
            })
    else:
        items = []
        pagination = {}
    return render(request, 'search.html', {'items': items, 'pagination': pagination})
