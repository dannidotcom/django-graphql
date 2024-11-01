
import graphene
from django.contrib.auth.models import User

class ResetPassword(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        reset_token = graphene.String(required=True)
        new_password = graphene.String(required=True)

    def mutate(self, info, reset_token, new_password):
        # Recherche de l’utilisateur par reset_token (logique simplifiée)
        user = User.objects.first()  # Remplace ceci par la vraie logique de recherche
        if user:
            user.set_password(new_password)
            user.save()
            return ResetPassword(success=True)
        return ResetPassword(success=False)
