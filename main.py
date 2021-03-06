from services.sncf import Station

def main():
    paris_est = Station(87113001).get_arrivals()
    print(paris_est)

if __name__ == '__main__':
    main()
