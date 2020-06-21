from model.projects import Project

def test_create_project(app):
    app.session.login("administrator", "root")
    old_projects = app.projects.get_project_list()
    new_project = Project(name="NewProj", description="JustForTest")
    old_projects.append(new_project)
    app.projects.create_project(new_project)
    new_projects = app.projects.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)