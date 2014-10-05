from fabric.decorators import task

import acp_commander
import awstools

@task
def setup_awstools():
  acp_commander.setup()
  awstools.setup()
