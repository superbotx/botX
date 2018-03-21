"""
To export your work, first you need to import the work from
your own source files
"""
from example_customized_componenet import ZedCameraComponent


"""
Then you need to compose an export module using your components
The module attribute is required and checked by the system, and
other parts are for documentation.
"""
botXexport = {
    'zed_camera': {
        'module': ZedCameraComponent,
        'type': 'api',
        'inputs': [],
        'outputs': [],
        'requirements': ['camera', 'ros'],
        'description': 'example api'
    },
}
