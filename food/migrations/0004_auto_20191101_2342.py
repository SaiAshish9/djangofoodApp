# Generated by Django 2.2.6 on 2019-11-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20191101_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwjo8JezzcnlAhXEPo8KHZUUC3EQjRx6BAgBEAQ&url=https%3A%2F%2Fwurtsmithairmuseum.net%2Fproduct%2Fusaf-veteran-license-metal-plate-frame%2F&psig=AOvVaw0ghMNpxu5LigvZHDDycfL0&ust=1572718000211418', max_length=500),
        ),
    ]
