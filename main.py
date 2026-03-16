import logging

logger: logging.Logger = logging.getLogger(__name__)


def main():
    logger.info('Hello from pimp-my-python-env!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
