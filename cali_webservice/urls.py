"""cali_webservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from views import base_api, search_engine

urlpatterns = [
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/graph/?$', base_api.get_graph, name='get_graph'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/(?P<hashed_sets>[\w_@-]+)/compatible/?$', base_api.get_compatible, name='get_compatible'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/(?P<hashed_sets>[\w_@-]+)/compliant/?$', base_api.get_compliant, name='get_compliant'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/(?P<hashed_sets>[\w_@-]+)/datasets/?$', base_api.get_datasets_of_licenses, name='get_datasets_of_licenses'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/search/?$', base_api.get_license_search, name='get_license_search'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/(?P<hashed_sets>[\w_@-]+)/?$', base_api.get_license_by_hash, name='get_license_by_hash'),
    url(r'^api/(?P<graph>[\w_@-]+)/licenses/?$', base_api.license_path, name='licenses_path'),
    url(r'^api/(?P<graph>[\w_@-]+)/datasets/search/?$', base_api.get_dataset_search, name='get_dataset_search'),
    url(r'^api/(?P<graph>[\w_@-]+)/datasets/(?P<hashed_uri>[\w_@-]+)/?$', base_api.get_dataset_by_hash, name='get_dataset_by_hash'),
    url(r'^api/(?P<graph>[\w_@-]+)/datasets/?$', base_api.dataset_path, name='dataset_path'),
    url(r'^api/licenses/experiment/?$', base_api.add_license_experiment, name='experiment'),
    url(r'^ld/graph/?$', search_engine.ld_graph, name='ldgraph'),
    url(r'^ld/search?$', search_engine.ld_search, name='ldsearch'),
    url(r'^ld/?$', search_engine.ld_engine, name='ldengine'),
    url(r'^rep/graph/?$', search_engine.rep_graph, name='repgraph'),
    url(r'^rep/search?$', search_engine.rep_search, name='repsearch'),
    url(r'^rep/?$', search_engine.rep_engine, name='repengine'),
    url(r'^api/?$', search_engine.api, name='api'),
    url(r'^about/?$', search_engine.about, name='about'),
    url(r'', search_engine.about, name='index'),
]
