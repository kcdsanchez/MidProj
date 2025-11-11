# This is the second artifact for the Topic 5 TODO demo

def get_user_data_from_db(user_id):
    # This function is intentionally simple

    # TODO: Add a caching layer to this function
    print(f"Fetching user {user_id} from database...")
    return {'id': user_id, 'name': 'Test User'}


print("Utils.py loaded")
