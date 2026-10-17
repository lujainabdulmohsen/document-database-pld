from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["art_gallery"]
artworks = db["artworks"]

artworks.drop()

artworks.insert_many([
    {
        "title": "Desert Sunset",
        "year": 2026,
        "price": 1500,
        "artist": {
            "name": "Sara",
            "country": "Saudi Arabia"
        },
        "tags": ["desert", "sunset"]
    },
    {
        "title": "Blue Sea",
        "year": 2025,
        "price": 1200,
        "artist": {
            "name": "Mona",
            "country": "Saudi Arabia"
        },
        "tags": ["sea", "blue"]
    },
    {
        "title": "Green Forest",
        "year": 2024,
        "price": 900,
        "artist": {
            "name": "Lina",
            "country": "Jordan"
        },
        "tags": ["forest", "green"]
    }
])

print("INSERT")
for artwork in artworks.find({}, {"_id": 0}):
    print(artwork)

print("\nQUERY")
print(
    artworks.find_one(
        {"title": "Desert Sunset"},
        {"_id": 0}
    )
)

print("\nNESTED DOCUMENT QUERY")
for artwork in artworks.find(
    {"artist.country": "Saudi Arabia"},
    {"_id": 0}
):
    print(artwork)

print("\nUPDATE")
artworks.update_one(
    {"title": "Blue Sea"},
    {"$set": {"price": 1350}}
)
print(
    artworks.find_one(
        {"title": "Blue Sea"},
        {"_id": 0}
    )
)

print("\nDELETE")
artworks.delete_one({"title": "Green Forest"})
for artwork in artworks.find({}, {"_id": 0}):
    print(artwork)

client.close()
