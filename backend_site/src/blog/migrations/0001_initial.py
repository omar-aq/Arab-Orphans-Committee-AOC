# Generated by Django 2.2.6 on 2019-11-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='post/')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]