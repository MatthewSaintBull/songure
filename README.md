# Songure

> This doc helps you for a brainless configuration of the stack inside the docker-compose file. Following this doc step-by-step, you won't have any issue.

 ## 1
 ### Create a .env file
Inside the root folder of your project, create a .env file with these data in it

> DB_ROOT=<db_user>
> DB_PASS=<db_pass>

Remember that you have to replace <db_user> and <db_pass> with the credentials that you will use for the next steps about DB configuration

## 2
### Create config file for the communication between DB container and Backend Apis

open up a terminal inside the root folder of <b>songure</b> and type these commands

    $ cd songure-api/app/config/
    ...
    $ mv config.local.py config.py
    ...

Now, open it with this command: 
`$ nano config.py`

You have to replace the fields with your own data. 
Below the description about the fields.

    config = { 
        "dev": { # the environment. At the moment only dev leave it as is
            "db_host": "127.0.0.1", # the db host where its located. You can leave it as is if you decided to use everything in only one server
            "db_port": "27017", # the db port. Remember to replace it even in the Dockerfile and docker-compose.yml
            "db_name": "songure", # Your db name, you can replace as you want
            "db_admin": "admin", # db username. Replace it with the same username put inside the .env at the step 1
            "db_password": "password", # same as db username
            "google_client_id": "xxxxxx", # your google client id
            "google_secret_id":"xxxxxx" # your google secret key
        }
    }

## 3
### Deploy your stack! :rocket:

Now you're ready for the deployment! move into the <b>songure root folder</b> and launch this command

    $ docker-compose up -d --build

> If you want to delete everything, instead launch the following commands

    $ docker-compose down
    
    Stopping songure-api ... done
    Stopping mongo-db    ... done
    Removing songure-api ... done
    Removing mongo-db    ... done
    Removing network songure_default
    
    $ docker volume prune
    
    WARNING! This will remove all local volumes not used by at least one container.
    Are you sure you want to continue? [y/N] y
    Deleted Volumes:
    9a0f69bd90cf6bb6aafe88239b50ba144f6f972a30f8e04fb6f33f42aafef0f4
    aee3bf9d42f7d611ea606a15f4e4447680b378900a7da914e922770163e26877
    songure_db-backup
    songure_db
    
    Total reclaimed space: 315.2MB

    $ docker image prune
    WARNING! This will remove all dangling images.
    Are you sure you want to continue? [y/N] y



If you want to be sure that everything is clear, launch this commands and check the response; if it says that there are containers/volums/network about the songure stack, feel free to remove them!
	
```
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

$ docker volume ls
DRIVER              VOLUME NAME

$ docker image ls
REPOSITORY            TAG                 IMAGE ID            CREATED             SIZE
```


