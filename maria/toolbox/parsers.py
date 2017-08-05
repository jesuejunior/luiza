# encoding: utf-8
from rest_framework.parsers import JSONParser


class JSParser(JSONParser):
    """
        Javascript parser.
    """
    media_type = 'application/javascript'
