from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=50)),
                ('provider_link', models.URLField()),
                ('provider_logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=30)),
            ],
        ),
    ]