from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as rest_views
from . import views

router = routers.DefaultRouter()
router.register(r'blog', views.BlogPostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api-token-auth/', rest_views.obtain_auth_token),
]
