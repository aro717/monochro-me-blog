# Generated by Django 3.1.5 on 2021-11-12 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('is_dir', models.BooleanField(default=True, verbose_name='ディレクトリか')),
                ('src', models.FileField(blank=True, null=True, upload_to='', verbose_name='ファイルソース')),
                ('zip_depth', models.PositiveIntegerField(default=0, verbose_name='zipファイルの深さ')),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'is_dir': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='myuploader.composite', verbose_name='親ディレクトリ')),
            ],
            options={
                'ordering': ('-is_dir', 'name'),
            },
        ),
    ]
