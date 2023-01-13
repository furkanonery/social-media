from django.contrib.auth.models import User
from profiller.models import Profil, ProfilDurum
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def created_profil(sender, instance, created, **kwargs):
    print(instance.username, '----Created---', created)
    if created:
        Profil.objects.create(user=instance)

@receiver(post_save, sender=Profil)
def created_profil_durum(sender, instance, created, **kwargs):
    if created:
        ProfilDurum.objects.create(
            user_profil=instance,
            durum_mesaji = f'{instance.user.username} kulübe katıldı.'
            )