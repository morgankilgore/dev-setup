#!/usr/bin/python
import subprocess
import platform
import sys
import os


def get_os():
    return platform.system()


def main():
    operating_system = get_os()
    if operating_system == 'Darwin':
        mac_os = MacOS()
        #mac_os.install_homebrew()
        mac_os.install_cask()
        mac_os.install_git()
        mac_os.install_python3()
        mac_os.install_virtualenv()
        mac_os.install_spotify()
        mac_os.install_docker()
        mac_os.install_aws_cli()
        mac_os.install_postman()
        mac_os.install_zsh()
        mac_os.install_configure_oh_my_zsh()
        mac_os.configure_vim()
        mac_os.install_nerd_fonts()
        mac_os.install_chrome()
        mac_os.install_sublime3()
        mac_os.install_slack()
        mac_os.install_byobu()
    else:
        print('OS not supported')
        sys.exit(-1)


class GenericOS(object):
    def __init__(self):
        self.home_path = os.path.expanduser("~")
        self.current_dir = os.getcwd()

    def local_command(self, command):
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

    def file_exists(self, filepath):
        return os.path.isfile(filepath)


class MacOS(GenericOS):
    def install_homebrew(self):
        self.local_command(['/usr/bin/ruby', '-e', "\"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\""])

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
        self.local_command(['brew', 'install', 'wget'])
        self.local_command(['wget', "https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh", "-O", 'oh-my-zsh-install.sh'])
        with open('oh-my-zsh-install.sh', 'r') as f:
            oh_my_zsh_file = f.readlines()

        with open('oh-my-zsh-install.sh', 'w') as f:
            for line in oh_my_zsh_file:
                if "env zsh -l" not in line:
                    f.write(line)

        self.local_command(['chmod', '+x', 'oh-my-zsh-install.sh'])
        self.local_command(['/bin/bash', 'oh-my-zsh-install.sh'])
        zsh_home_path = '{}/.zshrc'.format(self.home_path)
        if self.file_exists(zsh_home_path):
            os.remove(zsh_home_path)
        os.symlink('{}/.zshrc'.format(self.current_dir), zsh_home_path)

    def configure_vim(self):
        self.local_command(['git', 'clone', 'https://github.com/VundleVim/Vundle.vim.git', '{}/.vim/bundle/Vundle.vim'.format(self.home_path)])

        vim_home_path = '{}/.vimrc'.format(self.home_path)
        if self.file_exists(vim_home_path):
            os.remove(vim_home_path)
        os.symlink('{}/.vimrc'.format(self.current_dir), vim_home_path)
        self.local_command(['pip3', 'install', 'powerline-status'])
        self.local_command(['pip3', 'install', 'flake8'])
        self.local_command(['vim', '+silent', '+PluginInstall', '+qall'])

    def install_chrome(self):
        self.local_command(['brew', 'cask', 'install', 'google-chrome'])

    def install_sublime3(self):
        self.local_command(['brew', 'cask', 'install', 'sublime-text'])

    def install_slack(self):
        self.local_command(['brew', 'cask', 'install', 'slack'])

    def install_git(self):
        self.local_command(['brew', 'install', 'git'])

    def install_nerd_fonts(self):
        self.local_command(['brew', 'tap', 'caskroom/fonts'])
        self.local_command(['brew', 'cask', 'install', 'font-hack-nerd-font'])

    def install_byobu(self):
        self.local_command(['brew', 'install', 'byobu'])


if __name__ == '__main__':
    main()
