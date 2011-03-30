# Django Facebook by Thierry Schellenbach (http://www.mellowmorning.com)

Login and registration functionality using the new facebook open graph api.

* Actually creates user models and profiles
* Robust facebook user data -> django account conversion

## Required django apps

* django.contrib.auth (Django core app, included)
* django-registration
* django-notify

## Additional dependencies

* python-cjson

## Implementation

### Step 1 - Settings

Define the settings in `django_facebook/settings.py` in your `settings.py` file.

### Step 2 - Url config

add

    url(r'^facebook/', include('django_facebook.urls')),

to your global `url.py` file.

### Step 3 - Ensure the FB JS api is available on all pages you want to login

[Facebook JS API](http://developers.facebook.com/docs/reference/javascript/)

To add this, you can use the provided tag by adding:

    {% load facebook_tags %}

near the top of your document, and then adding:

    {% load_facebook_sdk %}

at the bottom, just before the closing body tag. The code is stored in the template
<pre>facebook/load_sdk.html</pre>, so feel free to override it.

### Step 4 - Update your models

Create a profile model from `FacebookProfileModel` from `django-facebook/models.py`.

Add a post_save signal handler for `django.contrib.auth.models.User` like:

<pre>
from django.contrib.auth.models import User
def create_profile(sender, instance, created, **kwargs):
    if created == True:
        try:
            YourProfileModel.objects.get(user=instance)
        except:
            profile = YourProfileModel(user=instance)
            profile.save()
post_save.connect(create_profile, sender=User)
</pre>

In `settings.py` assign your model name to `AUTH_PROFILE_MODULE` then specify the
facebook authentication backend:

<pre>
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_facebook.auth_backends.FacebookBackend',
)
</pre>

### Step 5 - Template

See `examples/connect.html`.

For more details, see the [Facebook docs](http://developers.facebook.com/docs/).
