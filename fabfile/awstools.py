from fabric.api import run, cd, env
from fabric.context_managers import settings

def setup():
  with settings(user='root'):
    install_pip()
    install_s3cmd()
    install_awscli()

def install_pip():
  run("wget https://pypi.python.org/packages/source/s/setuptools/setuptools-6.0.2.tar.gz --no-check-certificate -O setuptools-6.0.2.tar.gz")
  run("tar zxfv setuptools-6.0.2.tar.gz")
  with cd("setuptools-6.0.2"):
    run("python setup.py install")
  run("rm -rf setuptools-6.0.2")
  run("wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz --no-check-certificate -O pip-1.5.6.tar.gz")
  run("tar zxfv pip-1.5.6.tar.gz")
  with cd("pip-1.5.6"):
    run("python setup.py install")
  run('rm -rf pip-1.5.6')

def install_s3cmd():
  run("pip install python-dateutil")
  run("pip install http://sourceforge.net/projects/s3tools/files/s3cmd/1.5.0-rc1/s3cmd-1.5.0-rc1.tar.gz/download")

def install_awscli():
  run("pip install awscli")
