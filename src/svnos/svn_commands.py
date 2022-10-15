import subprocess
import logging


class SVNError(Exception):
    """Base class for SVN errors."""


class SVNConnectionError(SVNError):
    """Raised when the connection to a SVN server cannot be established."""


class SVNSystemError(SVNError):
    """Raised when the SVN program is not accessible."""


class SVNOperationError(SVNError):
    """Raised when a SVN command fails."""


def _do_run_svn_command(cmd: str) -> str:

    logging.info(f"Running command: {cmd!r}")
    result = subprocess.run(cmd, capture_output=True, shell=True)
    if result.returncode != 0:
        raise SVNOperationError(
            f"SVN command failed (returncode = {result}).\n\n"
            f"STDOUT:\n{result.stdout!r}\n"
            f"STDERR:\n{result.stderr!r}\n"
        )
    return result.stdout


def check_svn() -> None:
    try:
        _do_run_svn_command("svn --version")
    except SVNOperationError as err:
        raise SVNSystemError("The 'svn' command is not found on the system.") from err


def check_repository(username: str, repository: str) -> None:
    try:
        _do_run_svn_command(f"svn info {repository} --username {username}")
    except SVNOperationError as err:
        raise SVNConnectionError(
            f"Could not connect to the repository {repository!r}."
        ) from err
