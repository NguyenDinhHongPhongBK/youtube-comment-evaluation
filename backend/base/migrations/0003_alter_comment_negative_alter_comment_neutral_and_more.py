# Generated by Django 4.2.2 on 2023-06-25 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_chat_image_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='negative',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='neutral',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='positive',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
