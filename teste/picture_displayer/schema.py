import graphene
from graphene_django.types import DjangoObjectType
from .models import Image

class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = '__all__'

class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)
    image = graphene.Field(ImageType, image_id=graphene.ID())

    def resolve_all_images(self, info, **kwargs):
        return Image.objects.all()
    def resolve_image(self, info, image_id):
        return Image.objects.get(pk=image_id)
   

class CreateImageMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        image = graphene.String()

    added_image = graphene.Field(ImageType, name=graphene.String(),image = graphene.String())
    ok = graphene.Boolean()
    def mutate(root, info, name, image):
        image = Image(name=name, image=image)
        image.save()
        ok = True
        return CreateImageMutation(added_image=image, ok=ok)

class UpdateImageMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        image = graphene.String()

    added_image = graphene.Field(ImageType, name=graphene.String(),image = graphene.String())
    ok = graphene.Boolean()

    def mutate(root, info, id, name, image):
        Image.objects.filter(pk=id).update(name= name, image=image)
        ok = True
        return CreateImageMutation(added_image=Image.objects.get(pk=id), ok=ok)

class DeleteImageMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    added_image = graphene.Field(ImageType, name=graphene.String(),image = graphene.String())
    ok = graphene.Boolean()

    def mutate(root, info, id):
        Image.objects.filter(id=id).delete()
        ok = True
        return CreateImageMutation(ok=ok)

class Mutations(graphene.ObjectType):
    create_image_mutation = CreateImageMutation.Field()
    update_image_mutaion = UpdateImageMutation.Field()
    delete_image_mutation = DeleteImageMutation.Field()