import os
import shutil
import stat

from pathlib import Path
from git import Repo


class GitHubService:

    CLONE_DIR = Path("repositories")

    @classmethod
    def remove_readonly(cls, func, path, _):

        os.chmod(
            path,
            stat.S_IWRITE
        )

        func(path)

    @classmethod
    def clone_repository(
        cls,
        github_url: str
    ) -> str:

        cls.CLONE_DIR.mkdir(
            exist_ok=True
        )

        repo_name = (
            github_url
            .rstrip("/")
            .split("/")[-1]
            .replace(".git", "")
        )

        repo_path = (
            cls.CLONE_DIR / repo_name
        )

        if repo_path.exists():

            shutil.rmtree(
                repo_path,
                onerror=cls.remove_readonly
            )

        Repo.clone_from(
            github_url,
            str(repo_path)
        )

        return str(repo_path)