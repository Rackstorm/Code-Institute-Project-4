""" Importing necessary modules. """
from django.apps import AppConfig

class RecipesConfig(AppConfig):
    """ Recipes app configuration class. """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipes'

    def ready(self):
        import recipes.signals
