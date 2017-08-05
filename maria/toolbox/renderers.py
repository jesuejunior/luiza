# encoding: utf-8

from rest_framework.renderers import JSONRenderer


class JSRenderer(JSONRenderer):
    """
        Json renderer.
    """
    media_type = 'application/javascript'
