# Generated by Django 2.2.12 on 2020-05-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(blank=True, help_text='A description to display with your portfolio.', null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='listed_locally',
            field=models.BooleanField(default=False, help_text='Your portfolio will be listed on the Students page and other students will be able to see it.'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='listed_publicly',
            field=models.BooleanField(default=False, help_text='Your portfolio will may listed publicly.'),
        ),
    ]
