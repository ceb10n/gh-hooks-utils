from pydantic import BaseModel

from ..enterprise import Enterprise
from ..installation import Installation
from ..organization import Organization
from ..repository import Repository
from ..user import User
from .installation_action_enum import InstallationActionEnum


class InstallationEvent(BaseModel):
    action: InstallationActionEnum
    enterprise: Enterprise | None = None
    installation: Installation | None = None
    organization: Organization | None = None
    repository: Repository | None = None
    repositories: list[Repository] | None = None
    requestes: User | None = None
    sender: User
