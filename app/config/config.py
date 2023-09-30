from yaml import safe_load


def get_db_settings(config_name: str="./app/config/config.yaml"):
    with open(config_name, 'r') as f:
        data = safe_load(f)
    
    return data["database"]


def get_db_url(config_name: str="./app/config/config.yaml"):
    db_settings = get_db_settings(config_name)

    return f"postgresql://{db_settings['POSTGRES_USER']}:"\
                        f"{db_settings['POSTGRES_PASSWORD']}@"\
                        f"{db_settings['POSTGRES_HOST']}/"\
                        f"{db_settings['POSTGRES_DB']}"
