from glob import glob
from pathlib import Path
from typing import Dict, List, Union

from odoo.modules.module import get_module_resource


def get_custom_icons_path(module_folder: str) -> List[Dict[str, Union[str, Path]]]:
    """RETORNA A LISTA CONTENDO A MODEL E O CAMINHO ABSOLUTO DOS ICONES CUSTOMIZADOS"""
    icons = list(map(
        lambda icon: icon.split(
            'ax4b_theme')[1], glob(
            (str(Path(get_module_resource(module_folder)) /
                 'static/src/img/icons' / '*.png'))
        )
    ))

    icons_lists = {k.split('/')[-1].split('.')[0]: k for k in icons}

    return icons_lists
