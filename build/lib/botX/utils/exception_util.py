class CreateProjectError(Exception):

    def __init__(self, err_msg, fix_msg):
        self.err_msg = err_msg
        self.fix_msg = fix_msg

    def help_msg(self):
        print('Error: ', self.err_msg)
        print('Suggested: ', self.fix_msg)
