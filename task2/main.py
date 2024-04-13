import argparse
from dotenv import dotenv_values
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import command_handlers

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Cats manager")

    subparsers = parser.add_subparsers(title="Commands", dest="command", required=True)

    subparsers.add_parser("list", help="List all cats")

    details_subparser = subparsers.add_parser(
        "details", help="Display details of the cat"
    )
    details_subparser.add_argument("-n", "--name", help="Cat's name", required=True)

    update_name_subparser = subparsers.add_parser(
        "update-age", help="Update the age of the cat"
    )
    update_name_subparser.add_argument("-n", "--name", help="Cat's name", required=True)
    update_name_subparser.add_argument(
        "-a", "--age", help="Cat's new age", required=True, type=int
    )

    add_feature_subparser = subparsers.add_parser(
        "add-feature", help="Add a feature to the cat"
    )
    add_feature_subparser.add_argument("-n", "--name", help="Cat's name", required=True)
    add_feature_subparser.add_argument(
        "-f", "--feature", help="Feature to add", required=True
    )

    delete_cat_subparser = subparsers.add_parser("delete", help="Delete a cat")
    delete_cat_subparser.add_argument("-n", "--name", help="Cat's name", required=True)

    subparsers.add_parser("delete-all", help="Delete all cats")

    args = parser.parse_args()
    return args


def get_cats_collection():
    try:
        config = dotenv_values(".env")
        uri = f"mongodb+srv://{config['USER']}:{config['PASSWORD']}@{config['HOST']}/?retryWrites=true&w=majority&appName={config['APP_NAME']}"

        client = MongoClient(uri, server_api=ServerApi("1"))

        return client.cats_db.cats
    except Exception as e:
        print("Error connecting to the database")
        print(e)


args = parse_args()

cats_collection = get_cats_collection()

match args.command:
    case "list":
        command_handlers.list_cats(cats_collection)
    case "details":
        command_handlers.display_cat_details(cats_collection, args.name)
    case "update-age":
        command_handlers.update_cat_age(cats_collection, args.name, args.age)
    case "add-feature":
        command_handlers.add_cat_feature(cats_collection, args.name, args.feature)
    case "delete":
        command_handlers.delete_cat(cats_collection, args.name)
    case "delete-all":
        command_handlers.delete_all_cats(cats_collection)
    case _:
        print("Unknown command")