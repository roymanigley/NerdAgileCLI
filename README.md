# NerdAgileCLI
> NerdAgileCLI is a Scrum project management tool. The project contains a backend (REST API) and a CLI client

## Features

### CLI

- [x] CRUD for all models
- [x] add `PATCH` command to only update single fields
- [ ] when invoking `sprint:show --id 1` display a Kanban board 
- [ ] add error handling to show a nice output to the user (stacktrace only when DEBUG is set to true)

### API
- [x] CRUD endpoints for all models
- [x] add a `PATCH` endpoint for every model
- [ ] make the Bearer token more secure

## Run REST API application

### Locally

#### Build (Initial)

    python3 -m venv .env
    ./build_local.sh

### Run
> after running the `run_local.sh` script will create a `postgres` database using docker will be booted, once the application is running, you need to add the group `API_USER` to every user who wants to access the API 

    ./run_local.sh

### Productive

### Required Environment Variables
    
    export APP_PROD='TRUE'
    export APP_DB_NAME='YOUR_DB_NAME'
    export APP_DB_USERNAME='YOUR_DB_USERNAME'
    export APP_DB_PASSWORD='YOUR_DB_PASSWORD'
    export APP_DB_PORT='YOUR_DP_PORT'
    export APP_SUPERUSER_NAME='YOUR_SUPERUSER_USERNAME'
    export APP_DATABASE_PASSWORD='YOUR_SUPERUSER_PASSWORD'
    export APP_SUPERUSER_EMAIL='YOUR_SUPERUSER_EMAIL'
    export APP_SECRET_KEY='YOUR_SECRET_KEY'
### Build (Initial)

    ./build_prod.sh

### Run

    ./run_prod.sh

## Run the CLI application

    Usage: main.py [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      comment:delete
      comment:new
      comment:show
      comment:update
      epic:delete
      epic:new
      epic:show
      epic:update
      feature:delete
      feature:new
      feature:show
      feature:update
      project:delete
      project:new
      project:show
      project:update
      sprint:delete
      sprint:new
      sprint:show
      sprint:update
      sub_task:delete
      sub_task:new
      sub_task:show
      sub_task:update
      task:delete
      task:new
      task:show
      task:update