# Generated by Django 2.2.17 on 2021-07-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data_roles', '0006_remove_role_based_access_control_switch'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisedataroleassignment',
            name='applies_to_all_contexts',
            field=models.BooleanField(default=False, help_text='If true, indicates that the user is effectively assigned their role for any and all contexts. Defaults to False.'),
        ),
    ]