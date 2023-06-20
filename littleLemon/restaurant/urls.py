from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('static/<name>', views.staticfiles, name='sttic'),
    path('menu/items', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
