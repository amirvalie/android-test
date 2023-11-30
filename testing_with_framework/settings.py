# coding: utf8
import os
import yaml
import yml

if os.path.exists(os.path.dirname(__file__) + "/yml/config.yml"):
    env = os.environ.get('env', 'production')
    env = env.lower()
    if env in ['production']:
        CONFIG = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/config.yml", 'r'))[env]
        TEST_DATA = yaml.safe_load(open(os.path.dirname(__file__) + "/yml/{}.yml".format(env)))
    else:
        raise("Invalid Environment")
else:
    raise("config.yml does not exists")

platform = (CONFIG['platform'])