from registration.backends.simple.views import RegistrationView


# Subclassing django-registration-redux' RegistrationView
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return('registration_create_film')
