
from django.urls import path, include
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo api",
        default_version='1.0.0',
        description="API documentation of app",
    ),
    public=True
)


urlpatterns = [
    path('',views.getRoutes),
    path('show/',views.show),
    path('show/<str:pk>/',views.showItem),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name="swagger-schema")
    
   
]