from uuid import uuid4
import logging

logger = logging.getLogger(__name__)


def get_document_slug(instance):
    return (f"{instance.title}{str(instance.uid).split('-')[0]}")


def get_document_share_slug(instance):
    return (f"{'share'}{str(instance.uid).split('-')[0]}")


