# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    ThinkOpen Solutions Brasil
#    Copyright (C) Thinkopen Solutions <http://www.tkobr.com>.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'SMTP Server Per User',
    'category': 'Mail',
    'description': "Configure one SMTP server account by user.",
    'author': 'ThinkOpen Solutions Brasil',
    'license': 'AGPL-3',
    'website': 'http://tkobr.com',
    'version': '2.0',
    'sequence': 10,
    'depends': [
        'base',
        'mail',
        # 'web_widget_one2many_tags',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_users_view.xml',
        'views/ir_mail_server_view.xml',
    ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'certificate': '',
}
