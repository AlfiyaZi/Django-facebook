from django.contrib.auth import backends
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

class FacebookBackend(backends.ModelBackend):
    def authenticate(self, facebook_id, facebook_email):
        '''
        Authenticate the facebook user by id AND facebook_email
        '''
        try:
            profile_string = settings.AUTH_PROFILE_MODULE
            profile_model = profile_string.split('.')
            profile_class = ContentType.objects.get(app_label=profile_model[0].lower(), model=profile_model[1].lower())
            profile = profile_class.get_object_for_this_type(facebook_id=facebook_id, user__email=facebook_email)
            return profile.user
        except:
            return None
