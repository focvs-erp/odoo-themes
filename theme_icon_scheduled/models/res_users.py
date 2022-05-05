# -*- coding: utf-8 -*-

from functools import partial
from pathlib import Path
from typing import Dict, List, Union

from odoo import _, api, models
from odoo.modules.module import get_module_icon

# Metodo que gera e constroi a lista de
# dicionários com as models e path dos icones
from .modules import get_custom_icons_path


class Users(models.Model):
    _inherit = ['res.users']
    _description = 'Update activity systray icons'

    # --> AX4B ############
    def build_activity_icons_path(self, icons_path: List[Dict[str, Union[str, Path]]], model_name: str) -> str:
        """RESPONSÁVEL POR MONTAR A LISTA DOS DIRETÓRIOS QUE ESTÃO OS ICONES USANDO O NOME DO MODULO.
            SE O ICONE NÃO FOR ENCONTRADO NA PASTA OU O NOME ESTIVER COM NOME ERRADO/DIFERENTE, 
            VAI USAR O ICONE PADRÃO ODOO."""
        return icons_path.get(model_name.split('.')[0], get_module_icon(model_name))

    @api.model
    def systray_get_activities(self):

        get_icon = partial(
            self.build_activity_icons_path,
            get_custom_icons_path(module_folder='theme_icon_scheduled')
        )
        activities = super().systray_get_activities()

        for activity in activities:
            activity['icon'] = get_icon(activity['model'])

        return activities
        # <-- AX4B ############
