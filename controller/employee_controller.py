from odoo import http
from odoo.http import request, Response
import json


class EmployeeController(http.Controller):

    @http.route(['/employee/json'], type='http', website=True, autu='public')
    def employee_json(self, **kwargs):
        employees = request.env['employee.card'].sudo().search([]).read(['first_name', 'last_name', 'personal_id', 'features'])

        for item in employees:
            features = request.env['employee.feature'].sudo().search([('employee', '=', item['id'])]).read(['name', 'employee'])
            features_json_dump = json.dumps(features, indent=4, sort_keys=True)
            feature_json = json.loads(features_json_dump)
            item['features'] = feature_json
        return Response(json.dumps(employees, indent=4, sort_keys=True), content_type="application/json;charset=utf-8", status=200,)


