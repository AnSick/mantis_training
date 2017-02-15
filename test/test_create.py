from model.project import Project

def test_create(app):
    old_projects = app.project.get_project_list()
    app.project.create(Project(name = app.random_string("name", 15), status = "2", global_inheritage=False, visible=1, description="hsdjkahsdkjash"))
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)