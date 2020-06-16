import graphene
from picture_displayer.schema import Query as image_query
from picture_displayer.schema import Mutations as image_mutation

class Query(image_query):
    pass

class Mutations(image_mutation):
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)