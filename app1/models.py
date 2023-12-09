from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TypeOfUser(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class UserTG(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, blank=True)
    type_of_user = models.ForeignKey(TypeOfUser, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.full_name


class VeteransAssistant(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, blank=True)
    type_of_user = models.ForeignKey(TypeOfUser, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.surname


class Question(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    veterans_assistant = models.ForeignKey(VeteransAssistant, on_delete=models.SET_NULL, null=True, blank=True)
    user_gt = models.ForeignKey(UserTG, on_delete=models.PROTECT, null=True, blank=True)
    text_question = models.TextField(null=True,)
