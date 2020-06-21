from selenium.common.exceptions import NoSuchElementException
from model.projects import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_list()
        project_list = []
        elements = wd.find_elements_by_css_selector("tr")
        if len(elements) <=9:
            return project_list
        elif len(elements)>9:
            row_name = ["tr.row-1", "tr.row-2"]
            for row in row_name:
                elems = wd.find_elements_by_css_selector(row)
                for elem in elems:
                    cells = elem.find_elements_by_css_selector("td")
                    try:
                        link = cells[0].find_element_by_tag_name("a").get_attribute("href")
                        project_name = cells[0].text
                        v = link.index("=")
                        project_id = link[v+1:len(link)]
                        project_description = cells[4].text
                        project_list.append(Project(id=project_id, name=project_name, description=project_description))
                    except NoSuchElementException:
                        pass
        return project_list

    def create_project(self, new_project):
        wd = self.app.wd
        self.open_project_list()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(new_project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(new_project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
