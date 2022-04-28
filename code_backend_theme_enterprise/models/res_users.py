# -*- coding: utf-8 -*-

from glob import glob
from pathlib import Path

from odoo import api, models
from odoo.modules.module import get_module_icon, get_module_resource


class Users(models.Model):
    _inherit = ['res.users']
    _description = 'Update activity systray icons'

    # --> AX4B ############
    def build_activity_icons_path(self, model_name: str) -> str:
        """RESPONSÁVEL POR MONTAR A LISTA DOS DIRETÓRIOS ONDE ESTÃO OS ICONES USANDO O NOME DO MODULO.
            SE O ICONE NÃO FOR ENCONTRADO NA PASTA OU O NOME ESTIVER DIFERENTE, 
            VAI USAR O ICONE DO ADDONS PADRÃO DO ODOO."""
        icons = map(
            lambda icon: icon.split(
                'ax4b_activity')[1], glob(
                (str(Path(get_module_resource('code_backend_theme_enterprise')) /
                     'static/src/img/icons' / '*.png'))
            )
        )

        icons_lists = {k.split('/')[-1].split('.')[0]: k for k in icons}

        return icons_lists.get(model_name.split('.')[0], get_module_icon(model_name))

    @api.model
    def systray_get_activities(self):
        ctx = super().systray_get_activities()
        
        for act in ctx:
            act.update(
                {
                    'icon': self.build_activity_icons_path(model_name=act['model'])
                }
            )

        return ctx
        # <-- AX4B ############
