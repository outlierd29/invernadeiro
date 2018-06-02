# Generated by Django 2.0.4 on 2018-06-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
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
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
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
                'db_table': 'django_admin_log',
                'managed': False,
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
                'db_table': 'django_content_type',
                'managed': False,
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
                'db_table': 'django_migrations',
                'managed': False,
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
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('idauditoria', models.IntegerField(primary_key=True, serialize=False)),
                ('idusuario', models.IntegerField()),
                ('tabla', models.CharField(max_length=255)),
                ('accion', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
                ('dataantigua', models.TextField()),
                ('datanueva', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('idcronograma', models.IntegerField(primary_key=True, serialize=False)),
                ('idmodulo', models.IntegerField()),
                ('horainicio', models.IntegerField()),
                ('horafin', models.IntegerField()),
                ('temperatura', models.FloatField()),
                ('humedadambiente', models.FloatField()),
                ('humedadtierra', models.FloatField()),
                ('concentracionco2', models.FloatField()),
                ('luz', models.BooleanField()),
                ('nivelagua', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('idfoto', models.IntegerField(primary_key=True, serialize=False)),
                ('idmodulo', models.IntegerField(blank=True, null=True)),
                ('ruta', models.CharField(max_length=255)),
                ('nombresinextension', models.CharField(max_length=255)),
                ('extension', models.CharField(max_length=255)),
                ('nombrefoto', models.CharField(max_length=255)),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Historiainvernadero',
            fields=[
                ('idhistoriainvernadero', models.IntegerField(primary_key=True, serialize=False)),
                ('idinvernadero', models.IntegerField()),
                ('nivelenergia', models.FloatField(blank=True, null=True)),
                ('niveltanqueagua', models.FloatField(blank=True, null=True)),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Historiamodulo',
            fields=[
                ('idhistoriamodulo', models.IntegerField(primary_key=True, serialize=False)),
                ('idmodulo', models.IntegerField()),
                ('temperatura', models.FloatField(blank=True, null=True)),
                ('humedadtierra', models.FloatField(blank=True, null=True)),
                ('humedadambiente', models.FloatField(blank=True, null=True)),
                ('nivelagua', models.FloatField(blank=True, null=True)),
                ('concentracionco2', models.FloatField(blank=True, null=True)),
                ('luz', models.NullBooleanField()),
                ('fecharegistro', models.DateTimeField()),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Historiapanel',
            fields=[
                ('idhistoriapanel', models.IntegerField(primary_key=True, serialize=False)),
                ('idpanel', models.IntegerField()),
                ('encendido', models.BooleanField()),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Historiaplanta',
            fields=[
                ('idhistoriaplanta', models.IntegerField(primary_key=True, serialize=False)),
                ('idplanta', models.IntegerField()),
                ('idzona', models.IntegerField()),
                ('humedad', models.FloatField()),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Historiasemilla',
            fields=[
                ('idhistoriasemilla', models.IntegerField(primary_key=True, serialize=False)),
                ('idsemilla', models.IntegerField()),
                ('idmodulo', models.IntegerField()),
                ('posx', models.IntegerField()),
                ('posy', models.IntegerField()),
                ('comentario', models.CharField(blank=True, max_length=255, null=True)),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Historiazona',
            fields=[
                ('idhistoriazona', models.IntegerField(primary_key=True, serialize=False)),
                ('idzona', models.IntegerField()),
                ('temperatura', models.FloatField(blank=True, null=True)),
                ('ph', models.FloatField(blank=True, null=True)),
                ('concentracionco2', models.FloatField(blank=True, null=True)),
                ('fecharegistro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Invernadero',
            fields=[
                ('idinvernadero', models.IntegerField(primary_key=True, serialize=False)),
                ('idadmin', models.IntegerField()),
                ('codigoinvernaderojson', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('fechacreacion', models.DateTimeField()),
                ('area', models.FloatField(blank=True, null=True)),
                ('niveltanqueaguaideal', models.FloatField(blank=True, null=True)),
                ('niveltanqueaguamin', models.FloatField(blank=True, null=True)),
                ('niveltanqueaguamax', models.FloatField(blank=True, null=True)),
                ('nivelenergiaideal', models.FloatField(blank=True, null=True)),
                ('nivelenergiamin', models.FloatField(blank=True, null=True)),
                ('nivelenergiamax', models.FloatField(blank=True, null=True)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
                ('condicionesshidas', models.NullBooleanField()),
                ('idusuarioauditado', models.IntegerField()),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Modulosemilla',
            fields=[
                ('idmodulo', models.IntegerField(primary_key=True, serialize=False)),
                ('codigomodulojson', models.IntegerField()),
                ('temperaturaideal', models.FloatField(blank=True, null=True)),
                ('temperaturamin', models.FloatField(blank=True, null=True)),
                ('temperaturamax', models.FloatField(blank=True, null=True)),
                ('humedadtierraideal', models.FloatField(blank=True, null=True)),
                ('humedadtierramin', models.FloatField(blank=True, null=True)),
                ('humedadtierramax', models.FloatField(blank=True, null=True)),
                ('humedadambienteideal', models.FloatField(blank=True, null=True)),
                ('humedadambientemin', models.FloatField(blank=True, null=True)),
                ('humedadambientemax', models.FloatField(blank=True, null=True)),
                ('concentracionco2ideal', models.FloatField(blank=True, null=True)),
                ('concentracionco2min', models.FloatField(blank=True, null=True)),
                ('concentracionco2max', models.FloatField(blank=True, null=True)),
                ('nivelaguaideal', models.FloatField(blank=True, null=True)),
                ('nivelaguamin', models.FloatField(blank=True, null=True)),
                ('nivelaguamax', models.FloatField(blank=True, null=True)),
                ('filas', models.IntegerField()),
                ('columnas', models.IntegerField()),
                ('fechacreacion', models.DateTimeField()),
                ('habilitado', models.BooleanField()),
                ('idusuarioauditado', models.IntegerField()),
                ('condicionesshidas', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Panelluz',
            fields=[
                ('idpanel', models.IntegerField(primary_key=True, serialize=False)),
                ('codigopaneljson', models.IntegerField()),
                ('idzona', models.IntegerField()),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('idpermiso', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrepermiso', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Permisoxrol',
            fields=[
                ('idrol', models.IntegerField(primary_key=True, serialize=False)),
                ('idpermiso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('idplanta', models.IntegerField(primary_key=True, serialize=False)),
                ('idtipoplanta', models.IntegerField()),
                ('idzona', models.IntegerField()),
                ('idsemilla', models.IntegerField(blank=True, null=True)),
                ('codigoplantajson', models.IntegerField()),
                ('fechacreacion', models.DateTimeField()),
                ('humedadmin', models.FloatField(blank=True, null=True)),
                ('humedadideal', models.FloatField(blank=True, null=True)),
                ('humedadmax', models.FloatField(blank=True, null=True)),
                ('idusuarioauditado', models.IntegerField()),
                ('condicionesshidas', models.NullBooleanField()),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrerol', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Semilla',
            fields=[
                ('idsemilla', models.IntegerField(primary_key=True, serialize=False)),
                ('idtipoplanta', models.IntegerField()),
                ('idmodulo', models.IntegerField()),
                ('fechacreacion', models.DateTimeField()),
                ('habilitado', models.BooleanField()),
                ('idusuarioauditado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipoplanta',
            fields=[
                ('idtipoplanta', models.IntegerField(primary_key=True, serialize=False)),
                ('nombrecomun', models.CharField(max_length=255)),
                ('nombrecientifico', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField()),
                ('idfoto', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipozona',
            fields=[
                ('idtipozona', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.IntegerField(primary_key=True, serialize=False)),
                ('idrol', models.IntegerField()),
                ('nombres', models.CharField(max_length=255)),
                ('apellidopaterno', models.CharField(max_length=255)),
                ('apellidomaterno', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=1)),
                ('fechanacimiento', models.DateTimeField()),
                ('nombreusuario', models.CharField(max_length=255)),
                ('contrasena', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('fechacreacion', models.DateTimeField()),
                ('idusuarioauditado', models.IntegerField()),
                ('habilitado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarioxinvernadero',
            fields=[
                ('idinvernadero', models.IntegerField(primary_key=True, serialize=False)),
                ('idusuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('idzona', models.IntegerField(primary_key=True, serialize=False)),
                ('idtipozona', models.IntegerField()),
                ('idinvernadero', models.IntegerField()),
                ('codigozonajson', models.IntegerField()),
                ('nombre', models.CharField(max_length=255)),
                ('area', models.FloatField(blank=True, null=True)),
                ('temperaturaideal', models.FloatField(blank=True, null=True)),
                ('temperaturamin', models.FloatField(blank=True, null=True)),
                ('temperaturamax', models.FloatField(blank=True, null=True)),
                ('phideal', models.FloatField(blank=True, null=True)),
                ('phmin', models.FloatField(blank=True, null=True)),
                ('phmax', models.FloatField(blank=True, null=True)),
                ('concentracionco2ideal', models.FloatField(blank=True, null=True)),
                ('concentracionco2min', models.FloatField(blank=True, null=True)),
                ('concentracionco2max', models.FloatField(blank=True, null=True)),
                ('fechacreacion', models.DateTimeField()),
                ('habilitado', models.BooleanField()),
                ('idusuarioauditado', models.IntegerField()),
                ('condicionesshidas', models.NullBooleanField()),
            ],
        ),
    ]
