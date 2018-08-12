from django.shortcuts import render
from .forms import SearchForm
import requests
import json
from urllib.parse import quote


def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        pagination, items = findItemsByKeywords(form.cleaned_data['search'])
    else:
        items = []
        pagination = {}

    return render(request, 'search.html', {'items': items, 'pagination': pagination})


def findItemsByKeywords(keyword):
    def shipping_cost(item: dict):
        if item['shippingInfo'][0]['shippingType'] == 'Free':
            return 'Free'
        elif item['shippingInfo'][0]['shippingType'] == 'Flat':
            return (item['shippingInfo'][0]['shippingServiceCost'][0]['@currencyId'] +
                    item['shippingInfo'][0]['shippingServiceCost'][0]['__value__'])
        elif item['shippingInfo'][0]['shippingType'] == 'Calculated':
            return 'Calculated'

    def price(item: dict):
        return (item['sellingStatus'][0]['currentPrice'][0]['@currencyId'] +
                item['sellingStatus'][0]['currentPrice'][0]['__value__'])

    r = requests.get("""
            http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=SAMPLE-paulsl-PRD-02466ad0e-95ff6e2e&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords={}&paginationInput.entriesPerPage=100
            """.format(quote(keyword)))

    resp_str = r.content.decode('utf-8')
    result = json.loads(resp_str)['findItemsByKeywordsResponse'][0]
    pagination = {
        'pageNumber': result['paginationOutput'][0]['pageNumber'][0],
        'entriesPerPage': result['paginationOutput'][0]['entriesPerPage'][0],
        'totalPages': result['paginationOutput'][0]['totalPages'][0],
        'totalEntries': result['paginationOutput'][0]['totalEntries'][0]
    }
    items = []
    for item in result['searchResult'][0]['item']:
        items.append({
            'itemId': item['itemId'],
            'title': item['title'],
            'galleryURL': item['galleryURL'],
            'viewItemURL': item['viewItemURL'],
            'shipping_cost': shipping_cost(item),
            'price': price(item)
        })
    return pagination, items
