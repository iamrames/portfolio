from . import views
from django.urls import path

urlpatterns = [
    path("",views.index.as_view(),name='index'),
    path("about/",views.about.as_view(),name="about"),
    path("contact/",views.form_name_view,name="contact"),
    path("portfolio/",views.portfolio.as_view(),name="portfolio"),
    path("photos/",views.photos.as_view(),name="photos"),
    path("rames/",views.rames.as_view(),name="rames"),
]
