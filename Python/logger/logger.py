"""Python script to test logging
"""
import logging

def main():
    logger = logging.getLogger('testLogger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler('mylog.log')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.info('2   This is an info message')



if __name__ == "__main__":
    main()
