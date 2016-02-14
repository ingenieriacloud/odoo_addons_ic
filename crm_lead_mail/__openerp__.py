# -*- coding: utf-8 -*-
##############################################################################
#    crm_lead_mail
#    Copyright (c) 2016 Francisco Manuel García Claramonte <francisco@garciac.es>
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
    'name': 'Asignación automática de Iniciativas',
    'version': '8.0.0.1.0',
    'author': 'SerInCloud',
    'category': 'SerInCloud',
    'website': 'http://serincloud.org',
    'license': 'AGPL-3',
    'depends': ['crm','mail'],
    'description': """
Módulo para asignar las iniciativas que se reciben por correo
=============================================================

    Este módulo permite asignar Iniciativas recibidas por correo al empleado remitente. 
    Si la dirección de remite se corresponde con un comercial se le asígna automáticamente si no se deja sin asignar. 

    Publicado bajo licencia AGPL-v3
   
    Copyright (c) 2015-2016 Ingeniería Cloud

    Copyright (c) 2015-2016 Francisco Manuel García Claramonte

    """,

}

