
from graphene import ObjectType, Schema
from socialNet_backend.api.graphql.schema.user import UserQuery, UserMutation


class RootQuery(
    UserQuery,
    ObjectType
):
    pass


class RootMutation(
    UserMutation,
    ObjectType
):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
