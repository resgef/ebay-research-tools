from django.shortcuts import render


def examples(request):
    return render(request, 'search.html')

def find_item_by_keyword(keyword):
