from django.views.generic import TemplateView


class HomeView(TemplateView):
    """
    View to display our home page.
    """
    template_name = "pypi_app/home.html"
