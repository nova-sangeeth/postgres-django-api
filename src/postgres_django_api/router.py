from api.viewsets import userinfo_viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('userinfo', userinfo_viewset)
