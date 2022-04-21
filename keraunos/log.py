import logging


logger = logging.getLogger("keraunos")


def setup():
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    debug_file_handler = logging.FileHandler("log/debug.log")
    debug_file_handler.setLevel(logging.DEBUG)
    debug_file_handler.setFormatter(formatter)

    info_file_handler = logging.FileHandler("log/info.log")
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(debug_file_handler)
    logger.addHandler(info_file_handler)
