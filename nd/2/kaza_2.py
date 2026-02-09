import json
from pprint import pprint

from pymongo import MongoClient

# {"address": {"building": "1007", "coord": [-73.856077, 40.848447], "street": "Morris Park Ave", "zipcode": "10462"}, "borough": "Bronx", "cuisine": "Bakery", "grades": [{"date": {"$date": 1393804800000}, "grade": "A", "score": 2}, {"date": {"$date": 1378857600000}, "grade": "A", "score": 6}, {"date": {"$date": 1358985600000}, "grade": "A", "score": 10}, {"date": {"$date": 1322006400000}, "grade": "A", "score": 9}, {"date": {"$date": 1299715200000}, "grade": "B", "score": 14}], "name": "Morris Park Bake Shop", "restaurant_id": "30075445"}
# {"address": {"building": "469", "coord": [-73.961704, 40.662942], "street": "Flatbush Avenue", "zipcode": "11225"}, "borough": "Brooklyn", "cuisine": "Hamburgers", "grades": [{"date": {"$date": 1419897600000}, "grade": "A", "score": 8}, {"date": {"$date": 1404172800000}, "grade": "B", "score": 23}, {"date": {"$date": 1367280000000}, "grade": "A", "score": 12}, {"date": {"$date": 1336435200000}, "grade": "A", "score": 12}], "name": "Wendy'S", "restaurant_id": "30112340"}
# {"address": {"building": "351", "coord": [-73.98513559999999, 40.7676919], "street": "West   57 Street", "zipcode": "10019"}, "borough": "Manhattan", "cuisine": "Irish", "grades": [{"date": {"$date": 1409961600000}, "grade": "A", "score": 2}, {"date": {"$date": 1374451200000}, "grade": "A", "score": 11}, {"date": {"$date": 1343692800000}, "grade": "A", "score": 12}, {"date": {"$date": 1325116800000}, "grade": "A", "score": 12}], "name": "Dj Reynolds Pub And Restaurant", "restaurant_id": "30191841"}


def connect():
    try:
        db = client["pydb"]
        restaurants = db["restaurants"]
        return db, restaurants

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def insert_data(collection):
    # 1. Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)
    try:
        with open("restaurants.json", "r") as file:
            for line in file:
                entry = json.loads(line)
                restaurants.insert_one(entry)
            print("Data inserted!")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def display(results):
    pprint(results[:3], width=80)


def queries(collection):
    # 2. Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
    # display([x for x in collection.find()])

    # # 3. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
    # display(
    #     [
    #         x
    #         for x in collection.find(
    #             {}, {"restaurant_id": 1, "name": 1, "borough": 1, "cuisine": 1}
    #         )
    #     ]
    # )

    # # 4. Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko _id visiems dokumentams
    # display(
    #     [
    #         x
    #         for x in collection.find(
    #             {},
    #             {
    #                 "_id": 0,
    #                 "restaurant_id": 1,
    #                 "name": 1,
    #                 "borough": 1,
    #                 "cuisine": 1,
    #             },
    #         )
    #     ]
    # )

    # # 5. Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
    # display(
    #     [
    #         x
    #         for x in collection.find(
    #             {"borough": "Bronx"},
    #             {
    #                 "_id": 0,
    #                 "restaurant_id": 1,
    #                 "name": 1,
    #                 "borough": 1,
    #                 "cuisine": 1,
    #             },
    #         )
    #     ]
    # )

    # # 6. Parašykite užklausą, kuri parodytų restoranus su bendru įvertinimu tarp 80 ir 100 (duomenis gali reikėti agreguoti).
    # display(
    #     [
    #         x
    #         for x in collection.aggregate(
    #             [
    #                 {"$addFields": {"bendras": {"$sum": "$grades.score"}}},
    #                 {"$match": {"bendras": {"$gte": 80, "$lte": 100}}},
    #                 {
    #                     "$project": {
    #                         "name": 1,
    #                         "bendras": 1,
    #                         "grades": 1,
    #                         "cuisine": 1,
    #                         "borough": 1,
    #                     }
    #                 },
    #             ]
    #         )
    #     ]
    # )

    # # 7. Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
    # display(
    #     [
    #         x
    #         for x in collection.aggregate(
    #             [
    #                 {"$sort": {"cuisine": 1, "borough": -1}},
    #                 {
    #                     "$project": {
    #                         "name": 1,
    #                         "grades": 1,
    #                         "cuisine": 1,
    #                         "borough": 1,
    #                     }
    #                 },
    #             ]
    #         )
    #     ]
    # )

    pass


if __name__ == "__main__":
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db, restaurants = connect()

        if restaurants.count_documents({}) == 0:
            insert_data(restaurants)
        else:
            print("Data exits, skipping insertion!")

        queries(restaurants)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()

# insert_data()
