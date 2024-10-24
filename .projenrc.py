from projen.python import PythonProject

project = PythonProject(
    author_email="josysuarez2003@gmail.com",
    author_name="Jose Suarez",
    module_name="project_crud",
    name="project_crud",
    version="0.1.0",
)

project.synth()