# Generated by Django 4.1 on 2024-05-01 18:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LConduiteType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LInfraNature',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LInfraTypeLog',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LMasqueFace',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LPassageType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LPoseType',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LPtechNature',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LPtechTypeLog',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LPtechTypePhy',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LQualiteInfo',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='LTechnologieType',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=254)),
                ('definition', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TCheminement',
            fields=[
                ('cm_code', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('cm_codeext', models.CharField(max_length=254, null=True)),
                ('cm_cm1', models.CharField(max_length=254, null=True)),
                ('cm_cm2', models.CharField(max_length=254, null=True)),
                ('cm_r1_code', models.CharField(max_length=100, null=True)),
                ('cm_r2_code', models.CharField(max_length=100, null=True)),
                ('cm_r3_code', models.CharField(max_length=100, null=True)),
                ('cm_r4_code', models.CharField(max_length=100, null=True)),
                ('cm_voie', models.CharField(max_length=254, null=True)),
                ('cm_gest_do', models.CharField(max_length=20, null=True)),
                ('cm_prop_do', models.CharField(max_length=20, null=True)),
                ('cm_statut', models.CharField(max_length=3, null=True)),
                ('cm_etat', models.CharField(max_length=3, null=True)),
                ('cm_datcons', models.DateField(null=True)),
                ('cm_datemes', models.DateField(null=True)),
                ('cm_avct', models.CharField(max_length=1, null=True)),
                ('cm_typ_imp', models.CharField(max_length=2, null=True)),
                ('cm_compo', models.CharField(max_length=254, null=True)),
                ('cm_cddispo', models.IntegerField(null=True)),
                ('cm_fo_util', models.IntegerField(null=True)),
                ('cm_revet', models.CharField(max_length=254, null=True)),
                ('cm_remblai', models.CharField(max_length=254, null=True)),
                ('cm_charge', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cm_larg', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('cm_fildtec', models.BooleanField(null=True)),
                ('cm_mut_org', models.CharField(max_length=20, null=True)),
                ('cm_long', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('cm_lgreel', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('cm_comment', models.CharField(max_length=254, null=True)),
                ('cm_dtclass', models.CharField(max_length=2, null=True)),
                ('cm_geolqlt', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('cm_geolmod', models.CharField(max_length=4, null=True)),
                ('cm_geolsrc', models.CharField(max_length=254, null=True)),
                ('cm_creadat', models.DateTimeField(null=True)),
                ('cm_majdate', models.DateTimeField(null=True)),
                ('cm_majsrc', models.CharField(max_length=254, null=True)),
                ('cm_abddate', models.DateField(null=True)),
                ('cm_abdsrc', models.CharField(max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=3857)),
                ('cm_mod_pos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lposetype')),
                ('cm_nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.linfranature')),
            ],
        ),
        migrations.CreateModel(
            name='TConduite',
            fields=[
                ('cd_code', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('cd_codeext', models.CharField(max_length=254, null=True)),
                ('cd_etiquet', models.CharField(max_length=254, null=True)),
                ('cd_r1_code', models.CharField(max_length=100, null=True)),
                ('cd_r2_code', models.CharField(max_length=100, null=True)),
                ('cd_r3_code', models.CharField(max_length=100, null=True)),
                ('cd_r4_code', models.CharField(max_length=100, null=True)),
                ('cd_prop', models.CharField(max_length=20, null=True)),
                ('cd_gest', models.CharField(max_length=20, null=True)),
                ('cd_user', models.CharField(max_length=20, null=True)),
                ('cd_proptyp', models.CharField(max_length=3, null=True)),
                ('cd_statut', models.CharField(max_length=3)),
                ('cd_etat', models.CharField(max_length=3, null=True)),
                ('cd_dateaig', models.DateField(null=True)),
                ('cd_dateman', models.DateField(null=True)),
                ('cd_datemes', models.DateField(null=True)),
                ('cd_avct', models.CharField(max_length=1, null=True)),
                ('cd_dia_int', models.IntegerField(null=True)),
                ('cd_dia_ext', models.IntegerField(null=True)),
                ('cd_color', models.CharField(max_length=254, null=True)),
                ('cd_long', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('cd_nbcable', models.IntegerField(null=True)),
                ('cd_occup', models.DecimalField(decimal_places=0, max_digits=3, null=True)),
                ('cd_comment', models.CharField(max_length=254, null=True)),
                ('cd_creadat', models.DateTimeField(null=True)),
                ('cd_majdate', models.DateTimeField(null=True)),
                ('cd_majsrc', models.CharField(max_length=254, null=True)),
                ('cd_abddate', models.DateField(null=True)),
                ('cd_abdsrc', models.CharField(max_length=254, null=True)),
                ('cd_cd_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tconduite')),
                ('cd_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lconduitetype')),
            ],
        ),
        migrations.CreateModel(
            name='TPtech',
            fields=[
                ('pt_code', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('pt_codeext', models.CharField(max_length=254, null=True)),
                ('pt_etiquet', models.CharField(max_length=254, null=True)),
                ('pt_nd_code', models.CharField(max_length=254)),
                ('pt_ad_code', models.CharField(max_length=254, null=True)),
                ('pt_gest_do', models.CharField(max_length=20, null=True)),
                ('pt_prop_do', models.CharField(max_length=20, null=True)),
                ('pt_prop', models.CharField(max_length=20, null=True)),
                ('pt_gest', models.CharField(max_length=20, null=True)),
                ('pt_user', models.CharField(max_length=20, null=True)),
                ('pt_proptyp', models.CharField(max_length=3, null=True)),
                ('pt_statut', models.CharField(max_length=3)),
                ('pt_etat', models.CharField(max_length=3, null=True)),
                ('pt_dateins', models.DateField(null=True)),
                ('pt_datemes', models.DateField(null=True)),
                ('pt_avct', models.CharField(max_length=1, null=True)),
                ('pt_rf_code', models.CharField(max_length=254, null=True)),
                ('pt_secu', models.BooleanField(null=True)),
                ('pt_occp', models.CharField(max_length=10, null=True)),
                ('pt_a_dan', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('pt_a_dtetu', models.DateField(null=True)),
                ('pt_a_struc', models.CharField(max_length=100, null=True)),
                ('pt_a_haut', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('pt_a_passa', models.BooleanField(null=True)),
                ('pt_a_strat', models.BooleanField(null=True)),
                ('pt_rotatio', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('pt_detec', models.BooleanField(null=True)),
                ('pt_comment', models.CharField(max_length=254, null=True)),
                ('pt_creadat', models.DateTimeField(null=True)),
                ('pt_majdate', models.DateTimeField(null=True)),
                ('pt_majsrc', models.CharField(max_length=254, null=True)),
                ('pt_abddate', models.DateField(null=True)),
                ('pt_abdsrc', models.CharField(max_length=254, null=True)),
                ('pt_nature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lptechnature')),
                ('pt_typelog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lptechtypelog')),
                ('pt_typephy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lptechtypephy')),
            ],
        ),
        migrations.CreateModel(
            name='TNoeud',
            fields=[
                ('nd_code', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('nd_codeext', models.CharField(max_length=254, null=True)),
                ('nd_nom', models.CharField(max_length=254, null=True)),
                ('nd_r1_code', models.CharField(max_length=100, null=True)),
                ('nd_r2_code', models.CharField(max_length=100, null=True)),
                ('nd_r3_code', models.CharField(max_length=100, null=True)),
                ('nd_r4_code', models.CharField(max_length=100, null=True)),
                ('nd_voie', models.CharField(max_length=254, null=True)),
                ('nd_type', models.CharField(max_length=2, null=True)),
                ('nd_comment', models.CharField(max_length=254, null=True)),
                ('nd_dtclass', models.CharField(max_length=2, null=True)),
                ('nd_geolqlt', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('nd_geolmod', models.CharField(max_length=4, null=True)),
                ('nd_geolsrc', models.CharField(max_length=254, null=True)),
                ('nd_creadat', models.DateTimeField(null=True)),
                ('nd_majdate', models.DateTimeField(null=True)),
                ('nd_majsrc', models.CharField(max_length=254, null=True)),
                ('nd_abddate', models.DateField(null=True)),
                ('nd_abdsrc', models.CharField(max_length=254, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=3857)),
                ('nd_coderat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tnoeud')),
                ('nd_type_ep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ltechnologietype')),
            ],
        ),
        migrations.CreateModel(
            name='TMasque',
            fields=[
                ('mq_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mq_nd_code', models.CharField(max_length=254)),
                ('mq_col', models.IntegerField()),
                ('mq_ligne', models.IntegerField()),
                ('mq_comment', models.CharField(max_length=254, null=True)),
                ('mq_creadat', models.DateTimeField(null=True)),
                ('mq_majdate', models.DateTimeField(null=True)),
                ('mq_majsrc', models.CharField(max_length=254, null=True)),
                ('mq_abddate', models.DateField(null=True)),
                ('mq_abdsrc', models.CharField(max_length=254, null=True)),
                ('mq_cd_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.tconduite')),
                ('mq_face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lmasqueface')),
                ('mq_qualinf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lqualiteinfo')),
            ],
        ),
        migrations.CreateModel(
            name='TCondChem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dm_creadat', models.DateTimeField(null=True)),
                ('dm_majdate', models.DateTimeField(null=True)),
                ('dm_majsrc', models.CharField(max_length=254, null=True)),
                ('dm_abddate', models.DateField(null=True)),
                ('dm_abdsrc', models.CharField(max_length=254, null=True)),
                ('dm_cd_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condchem_conduites', to='app1.tconduite')),
                ('dm_cm_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='condchem_cheminements', to='app1.tcheminement')),
            ],
        ),
        migrations.AddField(
            model_name='tcheminement',
            name='cm_ndcode1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm_ndcode1_related', to='app1.tnoeud'),
        ),
        migrations.AddField(
            model_name='tcheminement',
            name='cm_ndcode2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cm_ndcode2_related', to='app1.tnoeud'),
        ),
        migrations.AddField(
            model_name='tcheminement',
            name='cm_passage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.lpassagetype'),
        ),
        migrations.AddField(
            model_name='tcheminement',
            name='cm_typelog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.linfratypelog'),
        ),
        migrations.AddConstraint(
            model_name='tcondchem',
            constraint=models.UniqueConstraint(fields=('dm_cd_code', 'dm_cm_code'), name='composite_primary_key'),
        ),
    ]
