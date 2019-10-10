# Generated by Django 2.2.6 on 2019-10-08 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archivist_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='logos')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archivist_app.Domains')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_link', models.URLField()),
                ('course_type', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=10)),
                ('Medium', models.CharField(choices=[('Video', 'Video'), ('Documents', 'Documents')], max_length=20)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archivist_app.Domains')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archivist_app.Keywords')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archivist_app.Course_Provider')),
            ],
        ),
    ]
