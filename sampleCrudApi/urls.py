from rest_framework import routers

from sampleCrudApi.views import PersonViewSet

personRouters = routers.DefaultRouter()


personRouters.register(r'persons', viewset=PersonViewSet)
