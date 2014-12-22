import os, sys
import getpass

from fabric.api import local, env
from fabric.operations import prompt
from fabric.network import needs_host
import fabric.state

jar_path = os.getcwd() + '/tmp/acp_commander.jar'

def download_jar():
  if not os.path.exists(jar_path):
    jar_url = 'http://downloads.buffalo.nas-central.org/TOOLS/ALL_LS_KB_ARM9/ACP_COMMANDER/acp_commander.jar'
    result = local('curl -s %s -o %s' % (jar_url, jar_path))

@needs_host
def setup():
  acp_run("sed -i 's/UsePAM yes/UsePAM no/g' /etc/sshd_config")
  acp_run("sed -i 's/PermitRootLogin no/PermitRootLogin yes/g' /etc/sshd_config")
  acp_run("(echo %s; echo %s)| passwd" % (env.password, env.password))
  acp_run("sed -i 's/SUPPORT_SFTP=0/SUPPORT_SFTP=1/g' /etc/nas_feature")
  acp_run("/etc/init.d/sshd.sh restart")

@needs_host
def acp_run(command):
  download_jar()
  env.password  = env.password or getpass.getpass(prompt='Input linkstation admin password:')
  acp_command = 'java -jar %s -q -t %s -ip %s -pw %s -c "%%s"' % (jar_path, env.host, env.host, env.password)
  local(acp_command % command)
