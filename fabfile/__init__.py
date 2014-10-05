from fabric.decorators import task

import acp_commander
import awstools

@task
def setup_ssh_only():
  acp_commander.setup()

@task
def run_cmd(cmd):
  acp_commander.acp_run(cmd)

@task
def setup_awstools():
  acp_commander.setup()
  awstools.setup()
