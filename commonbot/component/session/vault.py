import hvac


def get_secrets(vault_address: str, vault_path: str, vault_token: str):
    return hvac \
        .Client(url=vault_address, token=vault_token) \
        .secrets.kv.v1 \
        .read_secret(path=vault_path)
