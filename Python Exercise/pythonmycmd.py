from __future__ import print_function, division
import cmd


class mycmd(cmd.Cmd):
      prompt = 'CLI >>> '
      intro = 'Command Line Interpreter that can deploy, kill, benchmark and report'

      def do_deploy(self, line):
              print('Deployed')

      def help_deploy(self):
              print('To deploy')

      def do_kill(self, line):
              print('Killed')

      def help_kill(self):
              print('To kill')

      def do_benchmark(self, line):
              print('Benchmarked')

      def help_benchmark(self):
              print('To benchmark')

      def do_report(self, line):
              print('Reported')

      def help_report(self):
              print('To Report')
              
      def do_EOF(self, line):
              print('bye, bye')
              return True


if __name__ == '__main__':
      mycmd().cmdloop()
