
# Compile the image
docker build -t python-sre-bootcamp . 

# Execute the image
docker run -p 8080:8080 --rm -it python-sre-bootcamp

# One line for the previous steps
docker build -t python-sre-bootcamp . && docker run -p 8080:8000 --rm -it python-sre-bootcamp

# Export the env vars for not put on the repository
export DBHOST="sre-"
export DBSUER="user" 
export DBPASS="pass"
export DBDATABASE="database"

# Consume the API 
curl -X POST -d 'username=user&password=pass' localhost:8080/login
