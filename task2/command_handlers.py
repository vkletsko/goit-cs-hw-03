from pymongo.collection import Collection


def list_cats(cats_collection: Collection) -> None:
    for cat in cats_collection.find():
        print(cat)


def display_cat_details(cats_collection: Collection, name: str) -> None:
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Cat {name} not found")


def update_cat_age(cats_collection: Collection, name: str, age: int) -> None:
    update_result = cats_collection.update_one({"name": name}, {"$set": {"age": age}})
    if update_result.matched_count == 1:
        print(f"Updated the age of the cat {name} to {age}")
    else:
        print(f"Cat {name} not found")


def add_cat_feature(cats_collection: Collection, name: str, feature: str) -> None:
    update_result = cats_collection.update_one(
        {"name": name}, {"$push": {"features": feature}}
    )
    if update_result.matched_count == 1:
        print(f"Added feature {feature} to the cat {name}")
    else:
        print(f"Cat {name} not found")


def delete_cat(cats_collection: Collection, name: str) -> None:
    delete_result = cats_collection.delete_one({"name": name})
    if delete_result.deleted_count == 1:
        print(f"Deleted the cat {name}")
    else:
        print(f"Cat {name} not found")


def delete_all_cats(cats_collection: Collection) -> None:
    cats_collection.delete_many({})
    print("Deleted all cats")