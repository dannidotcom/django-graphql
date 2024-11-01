
import graphene
from django.core.mail import send_mail
from django.contrib.auth.models import User
import secrets

class ForgotPassword(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        email = graphene.String(required=True)

    def mutate(self, info, email):
        user = User.objects.filter(email=email).first()
        if user:
            reset_token = secrets.token_urlsafe()
            # Enregistre `reset_token` pour l'utilisateur (par ex., dans une table de token de réinitialisation)
            send_mail(
                'Réinitialisation du mot de passe',
                f'Utilisez ce token pour réinitialiser votre mot de passe : {reset_token}',
                'noreply@myapp.com',
                [email],
            )
        return ForgotPassword(success=True)
