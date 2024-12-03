# -*- coding: utf-8 -*-

from odoo import models, api

class CustomExport(models.Model):
    _inherit = 'ir.exports'

    @api.model
    def _prepare_export_data(self, fields, rows, model, options):
        data = super(CustomExport, self)._prepare_export_data(fields, rows, model, options)

        # Add company information to the beginning of the exported data
        company = self.env.company
        company_info = {
            'Company Name': company.name,
            'Company Address': company.street,
            'Company Phone': company.phone
        }

        # Insert company information at the beginning of the exported data
        rows.insert(0, company_info)

        return data

# from odoo import models, fields, api
#
#
# class IrExports(models.Model):
#     _inherit = 'ir.exports'
#
#     header = fields.Char(
#         string="Exporting header"
#     )
#
#     def generate_excel(self, cr, uid, ids, context=None):
#         """
#         Collect company information
#         """
#         company = self.env.user.company_id
#         """
#         Adding the company's information as header
#         """
#         self.write({'header': company.name + '\n' + company.address
#                     })
#         """
#         Generate the excel exportation
#         """
#         return super(IrExports , self).generate_excel(cr, uid, ids, context=context)



