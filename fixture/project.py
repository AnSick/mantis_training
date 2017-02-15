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