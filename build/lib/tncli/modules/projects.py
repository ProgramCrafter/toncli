import os
import shutil
import sys
from typing import Optional

from colorama import Fore, Style

from tncli.modules.utils.system.conf import project_root
from tncli.modules.utils.system.log import logger

gr = Fore.GREEN
rs = Style.RESET_ALL


class ProjectBootstrapper:
    ''' Create new folder and copy files from src/projects/{project} to this folder'''

    def __init__(self, project_name: str, folder_name: str, location: Optional[str] = None):
        self.project_name = project_name
        self.folder_name = folder_name

        self.project_location = f"{project_root}/projects"
        # current location where we need to create folder with project
        self.current_location = os.getcwd() if not location else location

    def deploy(self) -> None:
        logger.info(
            f"🐒 I'll create folder {gr}{self.current_location}/{self.folder_name}{rs} with project "
            f"{gr}{self.project_name}{rs} and all needed files")

        if not os.path.exists(f"{self.current_location}/{self.folder_name}"):
            os.mkdir(f"{self.current_location}/{self.folder_name}")  # create new project dir
        else:
            logger.error(
                f"🧨 Folder {self.current_location}/{self.folder_name} already exist, please use different one "
                f"(folder name can be defined by -n flag, e.g. -n my-wallet)")
            sys.exit()

        shutil.copytree(f"{self.project_location}/{self.project_name}", f"{self.current_location}/{self.folder_name}",
                        dirs_exist_ok=True)  # copy all from default project to new directory

        logger.info(f"👑 Folder {gr}successfully {rs}created - happy blockchain hacking")
        logger.info(
            f"🐼 You now can do {gr}cd {self.folder_name}{rs} and {gr}tncli deploy -n testnet{rs}")