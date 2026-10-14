#!/usr/bin/env python3

from pymongo import MongoClient
import os
import logging

# start logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# define variables from environment
MONGODB_ATLASURL = os.getenv('MONGODB_ATLAS_URL')
MONGODB_ATLASUSER = os.getenv('MONGODB_ATLAS_USER')
MONGODB_ATLASPWD = os.getenv('MONGODB_ATLAS_PWD')

# create the mongo client
client = MongoClient(MONGODB_ATLASURL, username=MONGODB_ATLASUSER, password=MONGODB_ATLASPWD)


def main():
    """start of the script. main() function"""
    try:
        db = client["bookstore"]
        authors_collection = db["authors"]
        books_collection = db["books"]

        author_ids_list = ["author_002", "author_003", "author_004"]
	#list of authors we care about. doesn't print the ones we don't care about

        logger.info("connected to MongoDB Atlas")

        # print number of authors in list
        author_num = authors_collection.count_documents({"_id": {"$in": author_ids_list}})
        print("Number of authors:", author_num)
        print("")

        # print each the authors and the books that they've written
        for author_id in author_ids_list:
            author = authors_collection.find_one({"_id": author_id})

            if author is None:
                print(f"{author_id} not found\n")
                continue

            print(author["name"])

            for book in books_collection.find({"author_ids": author_id}):
                print(f"  {book.get('title')} ({book.get('published_year')})")
            print("")

    except Exception as e:
        logger.error(f"Connection failed: {e}")
    finally:
        logger.info("Task complete.")
        client.close()


if __name__ == "__main__":
    main()
