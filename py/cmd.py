
import os


def main():
    print("main")
    os.chdir("C:/repos/pacteraedge/test/adf_to_synapse")
    print(os.getcwd())

    # write git command line commands
    c = os.system("git status")
    print(c)


if __name__ == "__main__":
    main()

