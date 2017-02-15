from model.project import Project
import random
import string

def test_delete(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(
            Project(name=app.random_string(prefix = "test", maxlen = 15), status="2", global_inheritage=False, visible=1, description="hsdjkahsdkjash"))
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)
