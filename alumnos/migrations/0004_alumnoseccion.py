# Generated by Django 3.2.12 on 2024-05-31 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_seccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoSeccion',
            fields=[
                ('id_alumnoseccion', models.AutoField(db_column='idAlumnoSeccion', primary_key=True, serialize=False)),
                ('id_alumno', models.ForeignKey(db_column='idRamo', on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno')),
                ('id_seccion', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='alumnos.seccion')),
            ],
        ),
    ]
