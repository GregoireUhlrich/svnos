from svn_client import SVNClient, SVNClientConfig


def main():
    config = SVNClientConfig.from_json("src\\svnos\\config.json")
    client = SVNClient(config=config)
    client.connect("amesim")


if __name__ == "__main__":
    main()
