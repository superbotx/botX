from botX.components import BaseComponent
from botX.applications import external_command_pool

class ZedCameraComponent(BaseComponent):

    def setup(self):
        """
        setup is the method we must implement which will be called
        in the robot interface
        """

        """
        The command is the same that you will execute in a terminal
        if path matters, you can either use an absolute path or a
        relative path from the project root
        """
        cmd = 'python fake_camera.py'

        """
        the start_command function will return a process id, so that
        you can stop the process when it is finished
        """
        proc_id = external_command_pool.start_command(cmd)

        """
        you will need to associate the returned process id with
        the object for later use
        """
        self.camera_proc_id = proc_id

    def shutdown(self):
        """
        Here you need to stop the process started in the setup
        """
        external_command_pool.end_command(self.camera_proc_id)
