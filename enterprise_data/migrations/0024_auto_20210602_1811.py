# Generated by Django 2.2.17 on 2021-06-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0023_enterpriselearner_enterpriselearnerenrollment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriselearnerenrollment',
            name='amount_learner_paid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='enterpriselearnerenrollment',
            name='course_list_price',
            field=models.FloatField(null=True),
        ),
    ]