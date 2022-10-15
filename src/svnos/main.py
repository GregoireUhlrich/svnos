from typing import List
from svn_client import SVNClient, SVNClientConfig
import cmd


class SVNTerm(cmd.Cmd):
    intro = "Welcome to SVNTerm! Because we want TortoiseSVN dead :)"
    prompt = "(svnterm) "

    def do_ls(self, line: str):
        self.stdout.write(f"Wow this is ls {line!r}!\n")

    def help_ls(self) -> str:
        print("List files in current location")

    def complete_ls(self, text: str, line: str, begin_idx, end_idx) -> List[str]:
        for w in ["Hello", "World"]:
            if w.startswith(text):
                return [w.lower()]
        return []

    def do_cd(self, line: str):
        self.stdout.write(f"Wow this is cd {line!r}!\n")

    def help_cd(self) -> str:
        print("Change directory")

    def do_pwd(self, line: str):
        self.stdout.write(f"Wow this is pwd {line!r}!\n")

    def help_ls(self) -> str:
        print("Print current location")

    def do_exit(self, line: str) -> bool:
        return True

    def help_exit(self):
        print("Exit SVNTerm")


def main():
    config = SVNClientConfig.from_json("src\\svnos\\config.json")
    client = SVNClient(config=config)
    # client.connect("amesim")

    SVNTerm().cmdloop()


if __name__ == "__main__":
    main()
