class Base(object):
    def __repr__(self):
        return "%r" % self.__dict__


class Container(Base):
    """Class to contain runtime attributes"""
    pass
