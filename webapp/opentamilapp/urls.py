"""opentamilweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index,name="home"),
    url(r'^translite/$', trans,name="translite"),
    url(r'^tsci/$', uni,name="tsci"),
    url(r'^keechu/$', keechu,name="keechu"),
    url(r'^spell/$', spl,name="spell"),
    url(r'^revers/$', rev,name="revers"),
    url(r'^number/$', num,name="number"),
    url(r'^anagram/$', anag,name="anagram"),
    url(r'^unigram/$', unig,name="unigram"),
    url(r'^ngram/$', ngra,name="ngram"),
    url(r'^vaypaadu/$',vaypaadu,name="multiplication"),
    url(r'^number/(?P<num>\d+)/$', numstr,name="numstr"),
    url(r'^tsci/(?P<tsci>.+?)/$', unicod,name="unicod"),
    url(r'^keechu/(?P<k1>.+?)/$', keech,name="keech"),
    url(r'^translite/(?P<tan>.+?)/$', translite,name="phonetic"),
    url(r'^spell/(?P<k1>.+?)/$', spell_check,name="spell_check"),
    url(r'^ngram/(?P<ng>.+?)', test_ngram,name="test_ngram"),
    url(r'^anagram/(?P<word>.+?)/$', anagram,name="ta_anagram"),
    url(r'^unigram/(?P<word>.+?)/$', test_basic,name="ta_unigram"),
    url(r'^revers/(?P<word>.+?)/$', revers,name="ta_revers"),
]
