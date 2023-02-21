# These functions need to be implemented
import mysql.connector
import jwt
import hashlib
import os


class Token:

    def generate_token(self, username, password):
        # Connect to MySQL database
        mydb = mysql.connector.connect(
            host=os.environ.get('DBHOST'),
            user=os.environ.get('DBSUER'),
            password=os.environ.get('DBPASS'),
            database=os.environ.get('DBDATABASE')
        )
        cursor = mydb.cursor()
        print(cursor)
        
        # Execute the query
        query = "SELECT username, password, salt, role FROM users WHERE username = %s"
        cursor.execute(query, (username,))

        # Fetch the results
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        mydb.close()

        print(result)
        if result is not None:
            # Get the stored salt and hash the provided password with it
            stored_salt = result[2]
            hashed_password = hashlib.sha512((password + stored_salt).encode('utf-8')).hexdigest()

            # Check if the hashes match
            if result[1] == hashed_password:
                # User authenticated, generate JWT access token
                payload = {'role': result[3]}
                secret_key = os.environ.get('JWTTOKEN')
                access_token = jwt.encode(payload, secret_key, algorithm='HS256')
                print("Access token:", access_token)
                return access_token
            else:
                print("Hashed passwords wrong")
        else:
            print("Invalid username or password")
        raise Exception ("Invalid username or password")


class Restricted:

    def access_data(self, authorization):
        try:
            # Verify the JWT token with the secret key
            secret_key = os.environ.get('JWTTOKEN')
            decoded_token = jwt.decode(authorization.replace('Bearer ', ''), secret_key, algorithms='HS256')

            # Check the contents of the JWT token
            print ("Current user from the token " + decoded_token['username'])
            return "You are under protected data"
        except jwt.exceptions.InvalidSignatureError:
            print("Token signature is invalid.")
        except jwt.exceptions.DecodeError:
            print("Unable to decode token.")
        except jwt.exceptions.InvalidTokenError:
            print("Token is invalid.")
        return "You can't access to this area"
