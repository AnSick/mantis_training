from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl +"api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self, username, password):
        client = Client(self.app.baseUrl +"api/soap/mantisconnect.php?wsdl")
        try:
            projectlist = list(client.service.mc_projects_get_user_accessible(username, password))
            projects = []
            for project in projectlist:
                projects.append(Project(id = project["id"], name = project["name"], description=project["description"],
                                        global_inheritage=project["enabled"], status = self.app.project.convert_status(project["status"]["name"]),
                                        visible=self.app.project.convert_visible(project["view_state"]["name"])))

            return projects
        except WebFault:
            print (WebFault)