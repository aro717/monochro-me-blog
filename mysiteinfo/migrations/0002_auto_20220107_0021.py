# Generated by Django 3.1.5 on 2022-01-06 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysiteinfo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitedetail',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='sitedetail',
            name='github',
        ),
        migrations.RemoveField(
            model_name='sitedetail',
            name='google_ad_html',
        ),
        migrations.AddField(
            model_name='sitedetail',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='アバター'),
        ),
        migrations.AddField(
            model_name='sitedetail',
            name='birthdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='生年月日'),
        ),
        migrations.AddField(
            model_name='sitedetail',
            name='job',
            field=models.CharField(default='管理者の職業', max_length=255, verbose_name='職業'),
        ),
        migrations.AlterField(
            model_name='sitedetail',
            name='email',
            field=models.EmailField(default='your_mail@gmail.com', max_length=255, verbose_name='アドレス'),
        ),
    ]
