VERSION={{ version }}
HOSTNAME={{ hostname }}
DB_USERNAME={{ db_username }}
DB_PASSWORD={{ db_password }}
ADMIN_USERNAME={{ admin_username }}
ADMIN_PASSWORD={{ admin_password }}
WORKSPACE_NAME={{ workspace_name }}
WORKSPACE_HOSTNAME={{ workspace_hostname }}
{% if use_proxy %}
WORKSPACE_PROXY_URL=http://10.0.3.15
{% endif %}