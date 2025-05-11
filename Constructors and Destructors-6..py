class Logger:
    def __init__(self):
        print("Logger object has been created!")

    def __del__(self):
        print("Logger object has been destroyed!")


logger1 = Logger()

del logger1

