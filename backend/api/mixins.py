from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny

from .permissions import IsAdminOrReadOnly
from recipes.models import Recipe
from .serializers import SubscribeRecipeSerializer

User = get_user_model()


class GetObjectMixin:
    serializer_class = SubscribeRecipeSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        recipe = get_object_or_404(Recipe, id=self.kwargs['recipe_id'])
        self.check_object_permissions(self.request, recipe)
        return recipe


class PermissionAndPaginationMixin:
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
