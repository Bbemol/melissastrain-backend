from services.sncf import Station, City

from utilities.list import List

def main():
    # paris_est = Station(87113001).get_arrivals()
    # print(paris_est)
    result = []

    paris_stations = City("Paris").get_stations()

    for station in paris_stations:
        name, id = List.filter(station, ["name", "id"]).values()
        arrivals = Station(id).get_arrivals()
        result.append({"name": name, "id": id, "arrivals": arrivals})

    print(result)

if __name__ == '__main__':
    main()
