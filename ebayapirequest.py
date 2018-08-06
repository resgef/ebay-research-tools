# -*- coding: utf-8 -*-
import requests


def build_headers(verb, compatibilityLevel, devID, appID, certID, siteID):
    h1 = {
        'X-EBAY-API-COMPATIBILITY-LEVEL ': compatibilityLevel,
        'X-EBAY-API-DEV-NAME ': devID,
        'X-EBAY-API-APP-NAME ': appID,
        'X-EBAY-API-CERT-NAME ': certID,
        'X-EBAY-API-CALL-NAME ': verb,
        'X-EBAY-API-SITEID ': siteID
    }
    return h1


def send(verb, api_keys, xml):
    h1 = {
        'X-EBAY-API-COMPATIBILITY-LEVEL ': api_keys['compatibilityLevel'],
        'X-EBAY-API-DEV-NAME ': api_keys['devID'],
        'X-EBAY-API-APP-NAME ': api_keys['appID'],
        'X-EBAY-API-CERT-NAME ': api_keys['certID'],
        'X-EBAY-API-CALL-NAME ': verb,
        'X-EBAY-API-SITEID ': api_keys['siteID']
    }
    r = requests.post(api_keys['serverUrl'], headers=h1, data=xml)
    return r
