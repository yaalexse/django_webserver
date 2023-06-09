# Generated by Django 4.2.1 on 2023-06-01 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_authors_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('join_date', models.DateField(auto_now=True)),
                ('job', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'job'],
            },
        ),
        migrations.AlterField(
            model_name='codes',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.new_authors'),
        ),
        migrations.DeleteModel(
            name='Authors',
        ),
    ]
