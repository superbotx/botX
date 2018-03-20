from botX.components import BaseComponent
from botX.applications import external_command_pool

class ZedCameraComponent(BaseComponent):

    def setup(self):
        """
        setup is the method we must implement which will be called
        in the robot interface
        """
        self.camera_proc_id = external_command_pool.start_command('python fake_camera.py')

    def shutdown(self):
        external_command_pool.end_command(self.camera_proc_id)
