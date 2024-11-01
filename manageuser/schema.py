
import graphene
from users.schema import Query as UserQuery, Mutation as UserMutation

class Query(UserQuery, graphene.ObjectType):
    pass

class Mutation(UserMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
