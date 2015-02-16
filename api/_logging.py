import logging


def setup():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    l = logging.getLogger('Rest Client')
    l.setLevel(logging.DEBUG)
    h = logging.StreamHandler()
    h.setLevel(logging.DEBUG)
    h.setFormatter(formatter)
    l.addHandler(h)
    return l


logger = setup()