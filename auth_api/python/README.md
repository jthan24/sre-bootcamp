
# Compile the image
docker build -t python-sre-bootcamp . 

# Execute the image
docker run -p 8080:8080 --rm -it python-sre-bootcamp

# One line for the previous steps
docker build -t python-sre-bootcamp . && docker run -p 8000:8000 --rm -it python-sre-bootcamp

# Export the env vars for not put on the repository
export DBHOST="sre-"
export DBSUER="user" 
export DBPASS="pass"
export DBDATABASE="database"

# Consume the login API 
curl -X POST -d 'username=user&password=pass' localhost:8000/login

# Create a var for TOKEN using the login API
export TOKEN=$(curl -X POST -d 'username=admin&password=secret' localhost:8000/login |jq .data -r )

# Consume the protected API
curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" localhost:8000/protected

# Execute all executions for the API in one line
TOKEN=$(curl -X POST -d 'username=admin&password=secret' localhost:8000/login |jq .data -r ) curl -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" localhost:8000/protected

