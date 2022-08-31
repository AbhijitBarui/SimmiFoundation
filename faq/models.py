from django.db import models


class faq(models.Model):
    def nameFile(instance, filename):
        return '/'.join(['FAQ', str(instance.question), filename])

    question=models.TextField()
    username=models.CharField(max_length=20)

    def __str__(self):
        return self.username
