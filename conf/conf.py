# -*- coding: utf-8 -*-

import os
import configparser as ConfigParser

cfg = ConfigParser.ConfigParser()
BASE_DIR = os.path.dirname(__file__)
cfg.read(os.path.join(BASE_DIR, 'config'))

# sqlserver
db_name_sqlserver = cfg.get("sqlServer_line", "db_name")
db_user_sqlserver = cfg.get("sqlServer_line", "db_user")
db_pass_sqlserver = cfg.get("sqlServer_line", "db_pass")
db_ip_sqlserver= cfg.get("sqlServer_line", "db_ip")
