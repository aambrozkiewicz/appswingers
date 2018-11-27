from rest_framework import routers

from django.urls import path
from contactlist import views

router = routers.DefaultRouter()
router.register('contacts', views.ContactViewSet, base_name='contacts')
urlpatterns = router.urls

urlpatterns += [
    path('magic-number', views.custom_list),
    path('cls-magic-number', views.ClassBasedMagicNumber.as_view()),
    path('custom-contacts', views.ContactsView.as_view()),

    path('custom-contacts/<int:pk>', views.ContactDetailView.as_view()),

    path('address/', views.AddressView.as_view()),
]
