""" Shows how to share logging configuration with a module """

import logging
import logging_pkg.my_logging_module


def main():
    # Both the lines in this file and in the imported package should log to the same file!
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    logging_pkg.my_logging_module.do_something()
    logging.info('Finished')


if __name__ == '__main__':
    main()


