"""MyTodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Todo.views import TodoViewSet, CheckListItemViewSet, LabelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# to handle check list items nested urls
from rest_framework_nested.routers import NestedDefaultRouter

router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todo')
router.register(r'labels', LabelViewSet, basename='label')
# router.register(r'checklist-items', CheckListItemViewSet, basename='checklistitem')

todos_router= NestedDefaultRouter(router, r'todos', lookup='todo')
todos_router.register(r'checklist-items', CheckListItemViewSet, basename='todo-checklistitem')
todos_router.register(r'labels', LabelViewSet, basename='todo-labels')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(todos_router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
