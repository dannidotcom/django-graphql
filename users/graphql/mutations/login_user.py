
import graphene
from django.contrib.auth.models import User
from graphql_jwt.shortcuts import get_token, create_refresh_token
from graphql import GraphQLError

class LoginUser(graphene.Mutation):
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password):
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise GraphQLError("Invalid credentials")
            token = get_token(user)
            refresh_token = create_refresh_token(user)
            return LoginUser(token=token, refresh_token=refresh_token)
        except User.DoesNotExist:
            raise GraphQLError("User not found")
