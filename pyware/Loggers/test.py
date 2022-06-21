from MouseLogger import MouseLogger, MouseCodes
from KeyboardLogger import KeyboardLogger, KeyboardCodes

if __name__ == '__main__':
    def test(*args):
        print(args)


    with MouseLogger(handler=test) as logger:
        logger.start_listener()

    # with KeyboardLogger(handler=test, quit_key=KeyboardCodes.KEY_P) as logger:
    #     logger.start_listener()
