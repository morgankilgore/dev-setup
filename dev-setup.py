#!/usr/bin/python
import subprocess
import platform
import sys
import os
import argparse


def get_os():
    return platform.system()


def main(args):
    operating_system = get_os()
    if operating_system == 'Darwin':
        mac_os = MacOS(action=args.action, zshrc_path=args.zshrc_path, vimrc_path=args.vimrc_path)
        if mac_os.action == 'install':
            #mac_os.install_homebrew()  # noqa 265
            mac_os.install_cask()
            mac_os.git()
            mac_os.python3()
            mac_os.virtualenv()
            mac_os.spotify()
            mac_os.docker()
            mac_os.aws_cli()
            mac_os.postman()
            mac_os.zsh()
            mac_os.configure_oh_my_zsh()
            mac_os.configure_vim()
            mac_os.nerd_fonts()
            mac_os.chrome()
            mac_os.sublime3()
            mac_os.slack()
            mac_os.byobu()
            mac_os.iterm2()
        else:
            mac_os.virtualenv()
            mac_os.spotify()
            mac_os.docker()
            mac_os.aws_cli()
            mac_os.postman()
            mac_os.zsh()
            mac_os.configure_oh_my_zsh()
            mac_os.configure_vim()
            mac_os.nerd_fonts()
            mac_os.chrome()
            mac_os.sublime3()
            mac_os.slack()
            mac_os.byobu()
            mac_os.iterm2()
            mac_os.git()
            mac_os.python3()

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
        if stderr:
            print("Error running '{}' command: {}".format(" ".join(command), stderr))

    def file_exists(self, filepath):
        return os.path.isfile(filepath)


class MacOS(GenericOS):
    def __init__(self, action, zshrc_path=None, vimrc_path=None):
        super(MacOS, self).__init__()

        self.action = action

        if zshrc_path is not None:
            self.zshrc_path = zshrc_path
        else:
            self.zshrc_path = '{}/.zshrc'.format(self.home_path)

        if vimrc_path is not None:
            self.vimrc_path = vimrc_path
        else:
            self.vimrc_path = '{}/.vimrc'.format(self.home_path)

    def install_homebrew(self):
        print('Installing homebrew...')
        self.local_command(['/usr/bin/ruby', '-e', "\"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)\""])

    def install_cask(self):
        print('Installing cask...')
        self.local_command(['brew', 'tap', 'caskroom/cask'])

    def spotify(self):
        print('{}ing spotify..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'spotify'])

    def docker(self):
        print('{}ing docker..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'docker'])

    def aws_cli(self):
        print('{}ing aws cli..'.format(self.action.capitalize()))
        self.local_command(['pip3', self.action, 'awscli'])

    def python3(self):
        print('{}ing python3..'.format(self.action.capitalize()))
        self.local_command(['brew', self.action, 'python'])

    def virtualenv(self):
        print('{}ing virtualenv..'.format(self.action.capitalize()))
        self.local_command(['pip3', self.action, 'virtualenv'])
        print('{}ing virtualenvwrapper..'.format(self.action.capitalize()))
        self.local_command(['pip3', self.action, 'virtualenvwrapper'])

    def postman(self):
        print('{}ing postman..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'postman'])

    def zsh(self):
        print('{}ing zsh..'.format(self.action.capitalize()))
        self.local_command(['brew', self.action, 'zsh'])

    def configure_oh_my_zsh(self):

        if self.action == 'install':
            print('{}ing wget..'.format(self.action.capitalize()))
            self.local_command(['brew', self.action, 'wget'])
            print('{}ing oh-my-zsh..'.format(self.action.capitalize()))
            self.local_command(['wget', "https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh", "-O", 'oh-my-zsh-install.sh'])
            with open('oh-my-zsh-install.sh', 'r') as f:
                oh_my_zsh_file = f.readlines()

            with open('oh-my-zsh-install.sh', 'w') as f:
                for line in oh_my_zsh_file:
                    if "env zsh -l" not in line:
                        f.write(line)

            self.local_command(['chmod', '+x', 'oh-my-zsh-install.sh'])
            self.local_command(['/bin/bash', 'oh-my-zsh-install.sh'])
            os.remove('oh-my-zsh-install.sh')
            if self.file_exists(self.zshrc_path):
                os.remove(self.zshrc_path)

            os.symlink('{}/.zshrc'.format(self.current_dir), self.zshrc_path)

        elif self.action == 'uninstall':
            print('{}ing oh-my-zsh..'.format(self.action.capitalize()))
            self.local_command(['uninstall_oh_my_zsh'])

    def configure_vim(self):
        print('{}ing powerline-status..'.format(self.action.capitalize()))
        self.local_command(['pip3', self.action, 'powerline-status'])
        print('{}ing flake8..'.format(self.action.capitalize()))
        self.local_command(['pip3', self.action, 'flake8'])

        if self.action == 'install':
            print('{}ing Vundle..'.format(self.action.capitalize()))
            self.local_command(['git', 'clone', 'https://github.com/VundleVim/Vundle.vim.git', '{}/.vim/bundle/Vundle.vim'.format(self.home_path)])

            vim_home_path = '{}/.vimrc'.format(self.home_path)
            if self.file_exists(vim_home_path):
                os.remove(vim_home_path)
            os.symlink('{}/.vimrc'.format(self.current_dir), vim_home_path)
            self.local_command(['vim', '+silent', '+PluginInstall', '+qall'])

        elif self.action == 'uninstall':
            if self.file_exists(self.vimrc_path):
                os.remove(self.vimrc_path)

    def chrome(self):
        print('{}ing chrome..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'google-chrome'])

    def sublime3(self):
        print('{}ing sublime3..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'sublime-text'])

    def slack(self):
        print('{}ing slack..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'slack'])

    def git(self):
        print('{}ing git..'.format(self.action.capitalize()))
        self.local_command(['brew', self.action, 'git'])

    def nerd_fonts(self):
        if self.action == 'install':
            self.local_command(['brew', 'tap', 'caskroom/fonts'])
        print('{}ing nerd fonts.'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'font-hack-nerd-font'])

    def byobu(self):
        print('{}ing byobu..'.format(self.action.capitalize()))
        self.local_command(['brew', self.action, 'byobu'])

    def iterm2(self):
        print('{}ing iterm2..'.format(self.action.capitalize()))
        self.local_command(['brew', 'cask', self.action, 'iterm2'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Installs software, tools, etc. needed for a basic dev environment.')
    parser.add_argument('--action', choices=['install', 'uninstall'], required=True, help='Option either to install or uninstall the basic dev environment.')
    parser.add_argument('--vimrc-path', required=False, help='Path to vimrc file. Default path is ~/.vimrc')
    parser.add_argument('--zshrc-path', required=False, help='Path to zshrc file. Default path is ~/.zshrc')
    args = parser.parse_args()
    main(args)
