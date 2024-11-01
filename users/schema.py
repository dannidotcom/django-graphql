# users/schema.py

import graphene
from .graphql.mutations.register_user import RegisterUser
from .graphql.mutations.login_user import LoginUser
from .graphql.mutations.forgot_password import ForgotPassword
from .graphql.mutations.reset_password import ResetPassword
from .graphql.queries.user_query import UserQuery

class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()
    login_user = LoginUser.Field()
    forgot_password = ForgotPassword.Field()
    reset_password = ResetPassword.Field()

class Query(UserQuery, graphene.ObjectType):
    pass
