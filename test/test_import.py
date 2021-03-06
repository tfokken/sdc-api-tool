from base_test_case import *
from sdctool import sdc_tool
import shlex
import uuid

pipe_id = uuid.uuid4()

def test_import(sdc):
    sdc_tool.run_with_args(
        shlex.split(
            'pipeline import --dest production --overwrite --pipelineJson testpipeline.json --pipelineId {}'.format(pipe_id)))


def test_export(sdc):
    sdc_tool.run_with_args(
        shlex.split(
            'pipeline export --src production --out test-results/pipeline-out.json --pipelineId {}'.format(pipe_id)))


def test_promote(sdc):
    sdc_tool.run_with_args(
        shlex.split(
            'pipeline promote --src production --srcPipelineId {} --dest production'.format(pipe_id)))
