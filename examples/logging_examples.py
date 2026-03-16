import logging

logger = logging.Logger(__name__)
# logger = logging.getLogger(__file__)
# logger = logging.getLogger(__name__)


def main():
    logging.debug("This is a debug message.")
    pass


if __name__ == "__main__":
    logger.setLevel(logging.WARN)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    main()
