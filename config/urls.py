from django.contrib import admin
from django.urls import path

#jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
#drf yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MY API",
      default_version='v000000000.0000001',
      description="no description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# my imports
from news.views import NewsViewSet, NewsListView, News2ListView
from accounts.views import RegisterViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register', RegisterViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('limitoffset/', NewsListView.as_view()),
    path('CustomPagination/', News2ListView.as_view()),
]

urlpatterns += router.urls
