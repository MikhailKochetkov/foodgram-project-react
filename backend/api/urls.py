from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (AddAndDeleteSubscribe, AddDeleteFavoriteRecipe,
                    AddDeleteShoppingCart, AuthToken, IngredientsViewSet,
                    RecipesViewSet, TagsViewSet, UsersViewSet, set_password)

app_name = 'api'

router = DefaultRouter()
router.register('ingredients', IngredientsViewSet)
router.register('recipes', RecipesViewSet)
router.register('tags', TagsViewSet)
router.register('users', UsersViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login/',
         AuthToken.as_view(),
         name='login'),
    path('recipes/<int:recipe_id>/favorite/',
         AddDeleteFavoriteRecipe.as_view(),
         name='favorite_recipe'),
    path('users/set_password/',
         set_password,
         name='set_password'),
    path('users/<int:user_id>/subscribe/',
         AddAndDeleteSubscribe.as_view(),
         name='subscribe'),
    path('recipes/<int:recipe_id>/shopping_cart/',
         AddDeleteShoppingCart.as_view(),
         name='shopping_cart'),
    path('', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
]
