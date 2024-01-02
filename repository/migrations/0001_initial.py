# Generated by Django 4.2.7 on 2023-12-29 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import repository.Utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='título')),
                ('description', models.TextField()),
                ('publication_date', models.DateField(auto_now=True)),
                ('author', models.CharField(max_length=255)),
                ('key_words', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='Documents/', validators=[repository.Utils.validate_file_extension])),
                ('image', models.ImageField(upload_to='Documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'documento',
            },
        ),
    ]