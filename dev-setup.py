#!/usr/bin/python
import subprocess
import platform
import sys
import shutil
import os


def get_os():
    return platform.system()


def main():
    operating_system = get_os()
    if operating_system == 'Darwin':
        mac_os = MacOS()
        mac_os.install_homebrew()
        mac_os.install_cask()
        mac_os.install_python3()
        mac_os.install_virtualenv()
        mac_os.install_spotify()
        mac_os.install_docker()
        mac_os.install_aws_cli()
        mac_os.install_postman()
        mac_os.install_zsh()
        mac_os.install_configure_oh_my_zsh()
        mac_os.configure_vim()
        mac_os.install_chrome()
        mac_os.install_sublime3()
        mac_os.install_slack()

    else:
        print('OS not supported')
        sys.exit(-1)


class GenericOS(object):
    def local_command(self, command):
        ret = subprocess.call(command)
        if ret == 1:
            print('Error running this command: {0}'.format(command))


class MacOS(GenericOS):
    def install_homebrew(self):
        self.local_command(['/usr/bin/ruby', '-e', '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'])

    def install_cask(self):
        self.local_command(['brew', 'tap', 'caskroom/cask'])

    def install_spotify(self):
        self.local_command(['brew', 'cask', 'install', 'spotify'])

    def install_docker(self):
        self.local_command(['brew', 'cask', 'install', 'docker'])

    def install_aws_cli(self):
        self.local_command(['pip3', 'install', 'awscli'])

    def install_python3(self):
        self.local_command(['brew', 'install', 'python'])

    def install_virtualenv(self):
        self.local_command(['pip3', 'install', 'virtualenv'])
        self.local_command(['pip3', 'install', 'virtualenvwrapper'])

    def install_postman(self):
        self.local_command(['brew', 'cask', 'install', 'postman'])

    def install_zsh(self):
        self.local_command(['brew', 'install', 'zsh'])

    def install_configure_oh_my_zsh(self):
        self.local_command(['sh', '-c', '"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"'])
        shutil.copy('.zshrc', '{}/.zshrc'.format(os.path.expanduser("~")))
        self.local_command('source', '~/.zshrc')

    def configure_vim(self):
        self.local_command(['git', 'clone', 'https://github.com/VundleVim/Vundle.vim.git', ' ~/.vim/bundle/Vundle.vim'])
        shutil.copy('.vimrc', '{}/.vimrc'.format(os.path.expanduser("~")))
        self.local_command(['vim', '-c', '"PluginInstall"', '-c', 'qa!'])
        self.local_command(['source', '~/.vimrc'])

    def install_chrome(self):
        self.local_command(['brew', 'cask', 'install', 'google-chrome'])

    def install_sublime3(self):
        self.local_command(['brew', 'cask', 'install', 'sublime-text'])

    def install_slack(self):
        self.local_command(['brew', 'cask', 'install', 'slack'])


if __name__ == '__main__':
    main()
