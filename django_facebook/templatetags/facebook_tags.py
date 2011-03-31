from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def load_facebook_sdk():
    return render_to_string("facebook/load_sdk.html", {"FACEBOOK_APP_ID": settings.FACEBOOK_APP_ID})


@register.simple_tag
def show_connect_button():
    return render_to_string("facebook/show_connect_button.html")
