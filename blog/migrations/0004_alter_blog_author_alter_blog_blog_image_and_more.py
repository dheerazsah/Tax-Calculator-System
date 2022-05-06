# Generated by Django 4.0.3 on 2022-05-06 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_blog_options_blog_blog_image_blog_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User '),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Featured Image'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Posted On:'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
    ]
