from model.projects import Project
import random

def test_delete_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    if (len(old_projects))==0:
        new_project = Project(name="NewProject", description="JustForTest")
        app.projects.create_project(new_project)
        old_projects = app.soap.get_project_list(username, password)
    proj = random.choice(old_projects)
    app.projects.delete_by_name(proj.name)
    old_projects.remove(proj)
    new_projects = app.soap.get_project_list(username, password)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

