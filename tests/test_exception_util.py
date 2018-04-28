from .botX.utils.exception_util import CreateProjectError

def test_error():
	oops = CreateProjectError("Project invalid.", "Fix project.")
	error = "Project invalid."
	fix = "Fix project."

	return error == oops.err_msg and fix == oops.fix_msg
