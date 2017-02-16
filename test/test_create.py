from model.project import Project

def test_create(app):
    old_projects = app.soap.get_project_list(app.username, app.password)
    project = Project(name = app.random_string("name", 15), status = "2", global_inheritage=False, visible=1, description="hsdjkahsdkjash")
    app.project.create(project)
    new_projects = app.soap.get_project_list(app.username, app.password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)