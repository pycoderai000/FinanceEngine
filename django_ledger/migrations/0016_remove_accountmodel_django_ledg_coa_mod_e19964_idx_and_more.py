# Generated by Django 5.0.4 on 2024-04-25 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0015_remove_chartofaccountmodel_locked_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='accountmodel',
            name='django_ledg_coa_mod_e19964_idx',
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_ledger.entitymodel', verbose_name='Ledger Entity'),
        ),
        migrations.AlterField(
            model_name='ledgermodel',
            name='ledger_xid',
            field=models.SlugField(allow_unicode=True, blank=True, help_text='User Defined Ledger ID', max_length=150, null=True, verbose_name='Ledger External ID'),
        ),
        migrations.AddIndex(
            model_name='accountmodel',
            index=models.Index(fields=['coa_model', 'code'], name='django_ledg_coa_mod_e073bc_idx'),
        ),
        migrations.AddIndex(
            model_name='accountmodel',
            index=models.Index(fields=['code'], name='django_ledg_code_081adc_idx'),
        ),
        migrations.AddIndex(
            model_name='ledgermodel',
            index=models.Index(fields=['entity', 'ledger_xid'], name='django_ledg_entity__7be095_idx'),
        ),
        migrations.AddIndex(
            model_name='ledgermodel',
            index=models.Index(fields=['ledger_xid'], name='django_ledg_ledger__05f099_idx'),
        ),
    ]
