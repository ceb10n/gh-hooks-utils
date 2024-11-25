import time

import jwt


def get_token(
    installation_id: int,
    *,
    cert: bytes | None = None,
    cert_path: str | None = None,
    exp: int = 600,
) -> str:
    """Creates a jwt token for github app installations.

    You should either pass cert or cert_path. If none is provided, an ValueError will
    be raised.

    Args:
        installation_id (int): The installation id for the github app
        cert (bytes, optional): The pem file of the github app. Defaults to None.
        cert_path (str, optional): The path of the pem file. Defaults to None.
        exp (int, optional): Token expiration. Must be less than 600. Defaults to 600.

    Raises:
        ValueError: Will raise a `ValueError` if:
            * If cert is not provided, neither the cert path
            * If installation id is `None`
            * If exp is greater than 600

    Returns:
        str: The jwt signed with the cert, to be used in the authentication process.
    """
    _raise_for_invalid_args(installation_id, cert, cert_path, exp)

    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + exp,
        "iss": installation_id,
    }

    signing_key = _get_cert(cert, cert_path)

    return jwt.encode(payload, signing_key, algorithm="RS256")


def _raise_for_invalid_args(
    installation_id: int,
    cert: bytes | None = None,
    cert_path: str | None = None,
    exp: int = 600,
) -> None:
    if not installation_id:
        raise ValueError("Github App installation id is required")

    if exp > 600:
        raise ValueError("Expiration must be lower than or equal to 600")

    if not cert and not cert_path:
        raise ValueError("cert or cert_path must be provided")


def _get_cert(cert: bytes | None, cert_path: str | None) -> bytes:
    if cert:
        return cert

    with open(str(cert_path), mode="rb") as f:
        return f.read()
