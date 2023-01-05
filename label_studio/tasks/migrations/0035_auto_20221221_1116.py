# Generated by Django 3.2.16 on 2022-12-21 11:16
import logging

from django.db import migrations

logger = logging.getLogger(__name__)


def forwards(apps, schema_editor):
    if not schema_editor.connection.vendor.startswith('postgres'):
        logger.info('Database vendor: {}'.format(schema_editor.connection.vendor))
        logger.info('Skipping dropping tasks_annotations_result_idx index')
        return

    schema_editor.execute('drop index if exists tasks_annotations_result_idx;')
    schema_editor.execute('drop index if exists tasks_annotations_result_idx2;')
    schema_editor.execute(
        'create index concurrently if not exists tasks_annotations_result_proj_gin '
        'on task_completion using gin (project_id, cast(result as text) gin_trgm_ops);'
    )


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [('tasks', '0034_auto_20221221_1101')]

    operations = [migrations.RunPython(forwards, backwards)]
