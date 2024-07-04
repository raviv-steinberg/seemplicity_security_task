from pathlib import Path


class Project:
    @staticmethod
    def get_rootpath() -> Path:
        """
        Returns the root path of the project.

        This function determines the root path of the project by
        getting the absolute path of the directory where this script
        is located.

        :return: The root path of the project as a Path object.
        :rtype: Path
        """
        return Path(__file__).parent.parent.parent.absolute()
