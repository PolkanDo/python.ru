# Generated by Django 2.0.1 on 2018-06-24 16:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Назовите баннер так, чтобы было удобно в дальнейшем определять его среди других баннеров', max_length=255, verbose_name='Название баннера')),
                ('file_swf', models.FileField(blank=True, null=True, upload_to='data/', verbose_name='Swf-файл')),
                ('file_img', models.FileField(blank=True, null=True, upload_to='data-img/', verbose_name='Файл изображения')),
                ('width', models.CharField(blank=True, help_text='Например, 100px, 720px или 100%', max_length=7, verbose_name='Ширина отображения баннера')),
                ('height', models.CharField(blank=True, help_text='Например, 100px, 200px или 100%', max_length=7, verbose_name='Высота отображения баннера')),
                ('link_to', models.CharField(help_text='Главная ссылка перехода.', max_length=255, verbose_name='Ссылка перехода')),
                ('date_from', models.DateField(default=django.utils.timezone.now, verbose_name='Дата старта показа баннеров')),
                ('date_to', models.DateField(help_text='В эту дату ещё будут показы.', verbose_name='Дата окончания показа баннеров')),
                ('date_days', models.IntegerField(default=254, help_text='Вычисляется как сумма: Понедельник = 2, Вторник = 4, Среда = 8, Четверг = 16, Пятница = 32, Суббота = 64, Воскресенье = 128. Для всей недели = 254, Только выходные = 192, Только будни = 62', verbose_name='Дни недели для показа')),
                ('date_time_from', models.IntegerField(default=0, help_text='Например, 12 или 20', verbose_name='Час начала показа каждый указанный день')),
                ('date_time_to', models.IntegerField(default=24, help_text='Не может быть меньше, чем час начала. Например, 12 или 20', verbose_name='Час окончания показа каждый указанный день')),
                ('priority', models.IntegerField(verbose_name='Приоритет показа от 1 до 100')),
                ('active', models.BooleanField(verbose_name='Активность баннера')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название места где будет размещатся банер')),
                ('tag', models.CharField(max_length=10, verbose_name='id где будет размещатся банер')),
            ],
            options={
                'verbose_name': 'Расположение',
                'verbose_name_plural': 'Расположение баннеров',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banners.Position', verbose_name='Место размещение банера'),
        ),
    ]
