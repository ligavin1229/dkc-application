from manage import *
from dkc.models import User
import query

class SearchHandler(AdminBaseHandler):

    def get(self):
        search = self.request.get('q')
        applicants = query.get_all_applicants()
        results = []
        for applicant in applicants:
            if self.match(applicant, search):
                results.append(applicant)

        template_values = {
            'q': search,
            'applicants': results,
            'admin_url': '/admin/search'
        }
        self.render_template('admin-search.html', template_values)

    def removeAttr(self, applicant, *args):
        applicant_info = str(applicant)
        for attr in args:
            index = applicant_info.find(attr)
            if attr in ["key", "application", "created", "updated"]:
                applicant_info = applicant_info[:index] + applicant_info[applicant_info.find(")")+2:]
            else:
                applicant_info = applicant_info[:index] + applicant_info[applicant_info.find(",", index)+1:]
        return applicant_info

    def match(self, applicant, search):
        applicant_info = [applicant.first_name, applicant.last_name, applicant.email, applicant.grade, applicant.address, applicant.city, applicant.zip_code, applicant.phone_number, applicant.division, applicant.ltg, applicant.school, applicant.school_address, applicant.school_city, applicant.school_zip_code, applicant.club_president, applicant.club_president_phone_number, applicant.faculty_advisor, applicant.faculty_advisor_phone_number]
        return search.lower() in "###".join(map(str, applicant_info)).lower()
