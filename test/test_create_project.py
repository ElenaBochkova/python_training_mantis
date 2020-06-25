from model.projects import Project
from datetime import datetime

def test_create_project(app):
    #app.session.login("administrator", "root")
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    new_project = Project(name="NewProj", description="JustForTest")
    while app.projects.project_is_in_list(proj=new_project, proj_list=old_projects):
        new_project = Project(name=str(datetime.now()), description="JustForTest")
    old_projects.append(new_project)
    app.projects.create_project(new_project)
    new_projects = app.soap.get_project_list(username, password)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)