import hashlib
import hmac
from typing import Any


def is_signature_valid(
    payload: dict[str, Any], secret: str, signature: str
) -> bool:
    """Validates the signature of the Github event.

    Args:
        payload (dict[str, Any]): Payload sent by github's webhook
        secret (str): Secret created by the owner of the app
        signature (str): The signature sent via header X-Hub-Signature-256

    Returns:
        bool: Returns true if the message is valid. Returns False otherwise.
    """
    hash_object = hmac.new(
        secret.encode("utf-8"),
        msg=payload,
        digestmod=hashlib.sha256,
    )

    expected_signature = "sha256=" + hash_object.hexdigest()

    return hmac.compare_digest(expected_signature, signature)
