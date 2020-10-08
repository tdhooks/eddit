import os
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0001_initial'),
    ]

    def add_su(apps, schema_editor):
        from django.contrib.auth.models import User

        su_uname = "admin"
        su_email = "jim@aol.com"
        su_pw = "Password@1"

        superuser = User.objects.create_superuser(
            username=su_uname,
            email=su_email,
            password=su_pw)

        superuser.save()

    operations = [
        migrations.RunPython(add_su),
    ]