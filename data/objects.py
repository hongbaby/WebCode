class Container(object):
    """Class to contain runtime attributes"""
    pass


class Student(object):
    username = None
    password = None
    member_id = None


class Product(object):
    def __init__(self):
        self.detail = {}

    partner = None
    product_id = None
    product_type = None
    main_red_code = None
    free_red_code = None
