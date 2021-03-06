# Generated by Django 2.2.1 on 2020-06-04 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tests', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_report', models.FileField(blank=True, null=True, upload_to='reports_PDF')),
                ('send_message', models.CharField(blank=True, max_length=250, null=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('approved_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.TestOrder')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
