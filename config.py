def main():
    try:
        configuration = open('config.txt')
    # except FileNotFoundError:
    #except Exception:
    #    print("Couldn't find the config.txt file!")
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError:
        print("You have not permission to open config.txt file")

if __name__ == '__main__':
    main()