from .botX.utils.exception_util.py import CreateProjectError

def test_error():
	oops = CreateProjectError(ValueError)
	error = "Your input value is invalid."
	fix = "Enter a value between 0.2 and 0.9."

	oops.__init__(self, error, fix)

	return error == oops.err_msg and fix == oops.fix_msg
