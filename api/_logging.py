import logging


def setup(name):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    l = logging.getLogger(name)
    l.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)
    h.setFormatter(formatter)
    l.addHandler(h)
    return l
