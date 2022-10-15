from __future__ import annotations

import json
from typing import Dict
from dataclasses import dataclass
from posixpath import join as urljoin
from svn_commands import check_svn, check_repository


class SVNClientConfigurationError(Exception):
    """Invalid SVN configuration."""


class SVNInvalidRepositoryError(Exception):
    """Raised when an invalid repository is used."""


@dataclass
class SVNClientConfig:
    username: str
    remote: str
    repositories: Dict[str, str]

    @staticmethod
    def from_json(filename: str) -> SVNClientConfig:
        with open(filename, "r") as file:
            data = json.loads(file.read())
            return SVNClientConfig(
                username=data["username"],
                remote=data["remote"],
                repositories=data["repositories"],
            )


class SVNClient:
    def __init__(self, config: SVNClientConfig) -> None:
        self.config = config

    def connect(self, repository: str) -> None:
        check_repository(
            username=self.config.username,
            repository=self.get_repository_path(repository),
        )

    def get_repository_path(self, repository: str) -> str:
        if not repository in self.config.repositories:
            raise SVNInvalidRepositoryError(f"Repository {repository!r} is invalid.")
        return urljoin(self.config.remote, self.config.repositories[repository])
