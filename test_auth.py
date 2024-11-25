import httpx

from gh_hooks_utils import auth

cert_path = "C:/Users/rafae/Downloads/know-my-devs.2024-11-21.private-key.pem"

with open(cert_path, "rb") as f:
    cert = f.read()


jwt = auth.app_authenticate(1065493, None, cert_path)
print(jwt)

headers = {
    "X-GitHub-Api-Version": "2022-11-28",
    "Authorization": f"Bearer {jwt}",
    "Accept": "application/vnd.github+json",
}

r = httpx.post("https://api.github.com/app/installations/57431416/access_tokens", headers=headers)

print(r.json())
