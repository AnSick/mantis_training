from model.project import Project

def test_create(app):
    app.project.go_to_project_management()
    app.project.create(Project(name = "test", status = "2", global_inheritage=False, visible=1, description="hsdjkahsdkjash"))
    assert app.session.is_logged_in_as("administrator")