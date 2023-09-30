from yaml import safe_load


def get_db_settings(config_name: str="./app/config/config.yaml"):
    with open(config_name, 'r') as f:
        data = safe_load(f)

    return data


def get_db_url(config_name: str="./app/config/config.yaml"):
    settings = get_db_settings(config_name)
    
    return f"postgresql://{settings['postgres_db']['user']}:"\
                        f"{settings['postgres_db']['password']}@"\
                        f"{settings['postgres_db']['host']}/"\
                        f"{settings['postgres_db']['db']}"
