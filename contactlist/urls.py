from rest_framework import routers

from contactlist import views

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet, base_name='contact')
urlpatterns = router.urls
