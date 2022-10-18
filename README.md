Simple app to manage event and notify on mail and phone SMS.

App will work on Raspberry Pi 4. 
To run the app .env file is required. Example:
```
DATABASE_USERNAME='postgres'
DATABASE_PASSWORD='password123'
DATABASE_HOST='db'
DATABASE_NAME='postgres'
```

Run the app using dokcer-compose: 
```commandline
docker-compose up --build
```

Use swagger on url: 
```commandline
localhost:[port]/docs/
```
