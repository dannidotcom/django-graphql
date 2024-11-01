
import graphene
from ..types import UserType
from django.contrib.auth.models import User

class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return User.objects.all()
