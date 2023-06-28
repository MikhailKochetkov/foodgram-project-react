class GetSubscribedMixin:

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return user.follower.filter(author=obj).exists()
        return False
