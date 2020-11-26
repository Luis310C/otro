# Generated by Django 3.1 on 2020-11-26 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuentasporcobrar', '0006_auto_20201125_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='nombre_de_la_Empresa',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='nombre_del_contacto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estilo',
            field=models.ForeignKey(default=({'id_estilo': 1},), on_delete=django.db.models.deletion.CASCADE, to='cuentasporcobrar.estilo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(default=({'id_rol': 2},), on_delete=django.db.models.deletion.CASCADE, to='cuentasporcobrar.rol'),
        ),
    ]
