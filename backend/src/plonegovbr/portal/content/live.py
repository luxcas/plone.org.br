from plone.dexterity.content import Container
from plone.supermodel.model import Schema


class ILiveVideo(Schema):
    """Uma série de conteúdo em vídeo."""


class LiveVideo(Container):
    """Uma série de conteúdo em vídeo."""
