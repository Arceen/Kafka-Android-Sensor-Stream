## Kafka Streamer
Stream real time sensor(Lat, Lng, altitude, etc.) data right into confluence kafka

Tech Stack -> Docker, Confluence Kafka + Zookeeper, Nginx, Flask, Python

### Steps to run
1) Install Docker Engine or Deskop (Just need to add it to path)
2) Clone the Repo to a project folder
3) `docker-compose up -d` or `docker-compose up` (Personally prefer attaching it into the current terminal for seeing the connection / backend)
4) Wait for the pull & it should run automatically.

### Project Orchaestration
Kafka is used to receive and distribute the realtime data. The nginx acts as a reverse proxy for the backend essentially hiding it. The flask backend simply acts like a producer. There's a standalone Android app written in Kotlin that produces this real-time data and supports this

### Operational Flow
The device hits the nginx server running on the local device. Currently mapped to port `8080` on the local device which is forwarded to the nginx container's `80` port. nginx just forwards that entire req along with routes into the backend container running a flask server on `8082` port. here we just take the data and put the json data as-is to the kafka producer (from python library)

### Known Issues & Fixes
Although the `kafka` dependency in `docker-compose.yml` for backend was added the `kafka` container might take a bit more time to load. If that's the case just start the backend using Docker desktop or terminal. You can see the list of processes running using `docker ps`. If you can't find anything resembling `backend`, just run it using terminal or desktop