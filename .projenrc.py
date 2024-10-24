from projen.python import PythonProject

project = PythonProject(
    author_email="josysuarez2003@gmail.com",
    author_name="Jose Suarez",
    module_name="project_crud",
    name="project_crud",
    version="0.1.0",
)

# Dependencias del proyecto
project.add_dependency("astroid==3.3.5")
project.add_dependency("blinker==1.8.2")
project.add_dependency("Brotli==1.1.0")
project.add_dependency("certifi==2024.8.30")
project.add_dependency("charset-normalizer==3.4.0")
project.add_dependency("click==8.1.7")
project.add_dependency("ConfigArgParse==1.7")
project.add_dependency("dill==0.3.9")
project.add_dependency("Flask==3.0.3")
project.add_dependency("Flask-Cors==5.0.0")
project.add_dependency("Flask-Login==0.6.3")
project.add_dependency("Flask-SQLAlchemy==3.1.1")
project.add_dependency("gevent==24.2.1")
project.add_dependency("geventhttpclient==2.3.1")
project.add_dependency("greenlet==3.1.1")
project.add_dependency("idna==3.10")
project.add_dependency("isort==5.13.2")
project.add_dependency("itsdangerous==2.2.0")
project.add_dependency("Jinja2==3.1.4")
project.add_dependency("linecache2==1.0.0")
project.add_dependency("locust==2.31.8")
project.add_dependency("MarkupSafe==2.1.5")
project.add_dependency("mccabe==0.7.0")
project.add_dependency("msgpack==1.1.0")
project.add_dependency("platformdirs==4.3.6")
project.add_dependency("psutil==6.0.0")
project.add_dependency("pylint==3.3.1")
project.add_dependency("python-dotenv==1.0.1")
project.add_dependency("pyzmq==26.2.0")
project.add_dependency("requests==2.32.3")
project.add_dependency("six==1.16.0")
project.add_dependency("SQLAlchemy==2.0.35")
project.add_dependency("tomlkit==0.13.2")
project.add_dependency("traceback2==1.4.0")
project.add_dependency("typing_extensions==4.12.2")
project.add_dependency("unittest2==1.1.0")
project.add_dependency("urllib3==2.2.3")
project.add_dependency("Werkzeug==3.0.4")
project.add_dependency("zope.event==5.0")
project.add_dependency("zope.interface==7.0.3")

# Dependencias de desarrollo
project.add_dev_dependency("coverage==7.6.3")
project.add_dev_dependency("setuptools==75.1.0")

project.synth()