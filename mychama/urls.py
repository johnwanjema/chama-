from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/edit$',views.update_profile,name='edit'),
    url('profile/', views.index, name='profile'),
    url('chama/create/', views.chama, name='create-chama'),
    url('loan/', views.loan, name='loan'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)