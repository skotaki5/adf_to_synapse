
import os


def main():
    print("main")
    os.chdir("C:/repos/pacteraedge/test/adf_to_synapse")
    print(os.getcwd())

    # write git command line commands
    c = os.system("git pull")
    print(c)
    c = os.system("git push")
    print(c)


if __name__ == "__main__":
    main()

