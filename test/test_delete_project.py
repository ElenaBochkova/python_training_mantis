from model.projects import Project
import random

def test_delete_project(app):
    old_projects = app.projects.get_project_list()
    if (len(old_projects))==0:
        new_project = Project(name="NewProject", description="JustForTest")
        app.projects.create_project(new_project)
        old_projects = app.projects.get_project_list()
    proj = random.choice(old_projects)
    app.projects.delete_by_name(proj.name)
    old_projects.remove(proj)
    new_projects = app.projects.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

