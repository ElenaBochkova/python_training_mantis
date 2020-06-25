from suds.client import Client
from suds import WebFault
from model.projects import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app
        self.base_url = self.app.config['web']['baseUrl'] + "/api/soap/mantisconnect.php?wsdl"

    def can_login(self, username, password):
        client = Client(self.base_url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.base_url)
        try:
            list_of_proj = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for proj in list_of_proj:
                projects.append(Project(id=proj.id, name=proj.name, description=proj.description))
            return projects
        except WebFault as e:
            print("WebFault " + str(e))
            return []
