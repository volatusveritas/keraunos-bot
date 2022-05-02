import logging
import os


logger = logging.getLogger("keraunos")


def setup_logging():
    if not os.path.exists("log"):
        os.mkdir("log")

    # Keraunos Bot
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

    # Discord.py
    dpy_logger = logging.getLogger("discord")

    dpy_file_handler = logging.FileHandler("log/discord.log")
    dpy_file_handler.setLevel(logging.DEBUG)
    dpy_file_handler.setFormatter(formatter)

    dpy_logger.setLevel(logging.DEBUG)
    dpy_logger.addHandler(dpy_file_handler)


def extension_loaded(name):
    logger.info(f"Extension loaded: {name}")


def extension_unloaded(name):
    logger.info(f"Extension unloaded: {name}")


def extension_reloaded(name):
    logger.info(f"Extension reloaded: {name}")
