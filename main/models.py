from django.db import models

from users.models import CustomUser
class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField(max_length=330, null=False, blank=False)
    message_sent_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.user.username} just received an anonymous message'