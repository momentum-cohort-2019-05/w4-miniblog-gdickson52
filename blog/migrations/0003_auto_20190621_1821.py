# Generated by Django 2.2.2 on 2019-06-21 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190621_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogger',
            options={'verbose_name_plural': 'My Blog Posts'},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name_plural': 'Bloggers Like Me'},
        ),
        migrations.RenameField(
            model_name='blogger',
            old_name='first_name',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogger',
            old_name='last_name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the blog', max_length=3500),
        ),
    ]