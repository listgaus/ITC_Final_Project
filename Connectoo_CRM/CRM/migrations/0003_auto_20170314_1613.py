# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_linkedcontacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group_permissions',
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_permission',
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_groups',
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user_user_permissions',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'django_content_type',
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.AlterModelOptions(
            name='agendas',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='attachments',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bulletinghosts',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bulletingroups',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bulletinlinks',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bulletinphotos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='bulletins',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='contacts',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='conversions',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventreminders',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='events',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventsingroups',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='eventtypes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='faces',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foodacts',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foodatgardens',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foods',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='foodtemplates',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='grouptypes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kgardens',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kidlacks',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kidphotos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kidpoops',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kidpresences',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kids',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='kindpoops',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lackatgardens',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lacks',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lacktemplates',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='likes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='messages',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='messagetemplates',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='numberofpics',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='numberofpicstags',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pictures',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='poops',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='profiles',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='relatives',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='schemamigrations',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='sleeps',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='timelines',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='userskids',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='versions',
            options={'managed': False},
        ),
    ]
