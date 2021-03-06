from services.sncf import get_stop_areas

def main():
    test = get_stop_areas(87113001)
    print(test)

if __name__ == '__main__':
    main()
