from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'myuploader'

router = DefaultRouter()
router.register(r'composites', views.CompositeViewSet, basename='composites')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/composites/get_composite_from_path/<path:request_path>', views.GetCompositeFromPath.as_view(), name='composites_frompath'),
    path('home/', views.serve, name='serve'),
    path('home/<path:request_path>', views.serve, name='serve'),
    path('zip/<int:pk>/', views.download_zip, name='download_zip'),
]
