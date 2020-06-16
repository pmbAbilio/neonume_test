import graphene
from picture_displayer.schema import Query as image_query

class Query(image_query):
    pass

schema = graphene.Schema(query=Query)