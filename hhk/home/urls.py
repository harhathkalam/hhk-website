from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('stories-of-hope/',views.stories_of_hope,name = 'stories-of-hope'),
    path('our-programs/',views.our_programs, name = 'our-programs'),
	path('about-us/',views.about_us,name = 'about-us'),
	path('connect-with-us/',views.connect_with_us,name = 'connect-with-us'),
	path('contact/',views.contact,name = 'contact'),
	path('our-team/',views.our_team,name = 'our-team'),
	path('donation/',views.donation,name = 'donation')
# Create your views here.

    ]