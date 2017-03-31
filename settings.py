"""
    File Name:settings.py
    Created On: 2017/03/31
    Description: This file contains some settings for ubiwifi, liking:
    databse configuration, app configuration, etc.
"""


class BaseConfig(object):
    """
       Description: about some base configuration.
    """
    DEBUG = True
    SECRET_KEY = "This secret key is used of ubiwifi"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/ubiwifi"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopConfig(BaseConfig):
    """
        Description: develop environment should use.
    """
    pass


class ProductConfig(BaseConfig):
    """
        Description: product environment should use.
    """
    DEBUG = False


app_config = {
    "develop": DevelopConfig,
    "product": ProductConfig
}


