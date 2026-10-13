#!/usr/bin/env python3

from pymongo import MongoClient
import os
import logging

# start logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# getting environment variables
ATLASURL = os.getenv('MONGODB_ATLAS_URL')
ATLASUSER = os.getenv('MONGODB_ATLAS_USER')
ATLASPASS = os.getenv('MONGODB_ATLAS_PWD')

# defining a mongo client
client = MongoClient(ATLASURL, username=ATLASUSER, password=ATLASPASS,
                     connectTimeoutMS=200, retryWrites=True)


def main():
    """complete tasks as listed in github instructions"""
    try:
        db = client["bookstore"]
        authors_collection = db["authors"]
        books_collection = db["books"]

        author_ids_list = ["author_002", "author_003", "author_004"]

        logger.info("Successfully connected to MongoDB Atlas")

        # print number of authors in list
        author_num = authors_collection.count_documents({"_id": {"$in": author_ids_list}})
        print("Number of authors:", author_num)
        print("")

        # print each author, along with their books
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
