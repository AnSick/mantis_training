from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.go_to_project_management()
        self.add_project(project)
        self.app.open_homepage()
        self.project_cache = None


    def go_to_project_management(self):
        wd = self.app.wd
        wd.get(self.app.baseUrl + 'manage_proj_page.php')

    def add_project(self,project):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/form/fieldset/input[2]').click()
        self.app.change_field_value("name", project.name)
        self.app.change_field_value("description",project.description)
        if not wd.find_element_by_xpath(
                        '//*[@id="project-status"]//option[%s]' % project.status).is_selected():
            wd.find_element_by_xpath('//*[@id="project-status"]//option[%s]' % project.status).click()
        if not wd.find_element_by_xpath(
                        '//*[@id="project-view-state"]//option[%s]' % project.visible).is_selected():
            wd.find_element_by_xpath('//*[@id="project-view-state"]//option[%s]' % project.visible).click()
        if project.global_inheritage is False:
            wd.find_element_by_xpath('//*[@id="manage-project-create-form"]/div/div[2]/div/div/table/tbody/tr[3]/td[2]/label/span').click()
        wd.find_element_by_css_selector('#manage-project-create-form > div > div.widget-toolbox.padding-8.clearfix > input').click()
        self.go_to_project_management()


    def convert_status(self, status):
        if status == "development":
            status == "1"
        elif status == "release":
            status = "2"
        elif status == "stable":
            status = "3"
        elif status == "obsolete":
            status = "4"
        return status

    def convert_visible(self, visible):
        if visible == "public":
            visible = "1"
        else:
            visible = "2"
        return visible

    project_cache = None
    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_project_management()
            self.project_cache = []
            table = wd.find_elements_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/table/tbody/tr')
            for element in table:
                data = element.find_elements_by_tag_name("td")
                name = data[0].text
                status = self.convert_status(data[1].text)
                visible = self.convert_visible(data[3].text)
                description = data[4].text
                id = wd.find_element_by_link_text(name).get_attribute("href").replace(self.app.baseUrl + "manage_proj_edit_page.php?project_id=", "")
                self.project_cache.append(Project(name = name, status = status, id = id, visible=visible, description = description))
        return list(self.project_cache)


    def delete_project(self, project):
        wd = self.app.wd
        wd.get(self.app.baseUrl + "manage_proj_edit_page.php?project_id="+str(project.id))
        wd.find_element_by_xpath('//*[@id="project-delete-form"]/fieldset/input[3]').click()
        wd.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/div/div/div[2]/form/input[4]').click()
        self.go_to_project_management()
        self.project_cache = None