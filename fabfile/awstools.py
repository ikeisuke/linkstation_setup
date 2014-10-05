from fabric.api import run, cd, env
from fabric.context_managers import settings

def setup():
  with settings(user='root'):
    setup_environment()
    install_s3cmd()
    install_awscli()

def setup_environment():
  run("wget http://peak.telecommunity.com/dist/ez_setup.py -O ez_setup.py")
  run("python ez_setup.py")
  run("easy_install setuptools")
  run("wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz#md5=01026f87978932060cc86c1dc527903e --no-check-certificate -O pip-1.5.6.tar.gz")
  run("tar zxfv pip-1.5.6.tar.gz")
  with cd("pip-1.5.6"):
    run("python setup.py install")
  run('rm -rf pip-1.5.6')

def install_s3cmd():
  run("pip install python-dateutil")
  run("wget http://sourceforge.net/projects/s3tools/files/s3cmd/1.5.0-rc1/s3cmd-1.5.0-rc1.tar.gz/download -O s3cmd-1.5.0-rc1.tar.gz")
  run("tar zxfv s3cmd-1.5.0-rc1.tar.gz")
  with cd("s3cmd-1.5.0-rc1"):
    run("python setup.py install")
  run("rm -rf s3cmd-1.5.0-rc1")

def install_awscli():
  run("pip install awscli")
