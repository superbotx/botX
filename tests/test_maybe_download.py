from .botX.utils.install_util import maybe_download_git
import os

def test_maybe_download_from_git():
    maybe_download_git('https://github.com/superbotx/.gazebo/archive/master.zip', os.environ['HOME'], '.gazebo')
