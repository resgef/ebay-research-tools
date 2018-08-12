#!/usr/bin/env python3
import sys, os, django

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_DIR))  # here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ebayresearch.settings")
django.setup()

from ebayresearch.views import findItemsByKeywords

findItemsByKeywords('harry potter')
