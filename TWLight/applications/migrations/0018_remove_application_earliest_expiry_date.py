# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("applications", "0017_auto_20170709_1859")]

    operations = [
        migrations.RemoveField(model_name="application", name="earliest_expiry_date")
    ]
