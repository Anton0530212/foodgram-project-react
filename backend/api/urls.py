from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet
from .views import IngredientViewSet, TagsViewSet, RecipeViewSet

app_name = 'api'
router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('tags', TagsViewSet, basename='tags')
router.register('ingredients', IngredientViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
