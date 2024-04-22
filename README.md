# Pokeberries API <img src="https://images.wikidexcdn.net/mwuploads/wikidex/3/30/latest/20240130175744/Baya_Frambu_%28Dream_World%29_2.png" height="27px" style="margin-bottom: -3px">

This is a Flask-based API for Pokeberries statistics.

## Getting Started

To run this API, follow these steps:

1. Install Python (if you haven't already).

2. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

   > You can first create a virtual environment to install the dependencies.

3. Run the Flask application:

   ```sh
   flask run
   ```

4. Access the API at http://localhost:5000.

## Run with Docker

To run this API with Docker, follow these steps:

1. Install [Docker](https://docs.docker.com/engine/install/) (if you haven't already).

2. Build the docker image:

   ```sh
   docker build -t test:latest .
   ```

3. Run the docker image:

   ```sh
   docker run test:latest
   ```

4. A Docker container is isolated from your host machine, meaning it operates with its own IP address, typically starting with 172. You can find it in your terminal after you start running the Docker container.

   Access the API at http://172.X.X.X:8000.

## Tests

You can run the unit tests of the project with the command:

```sh
  pytest tests
```

You can also run the tests from the docker image:

```sh
docker run test:latest pytest tests
```

## Endpoints

  <details>
  <summary><code>GET</code> <code><b>/</b></code> <code>(Returns a welcome message)</code></summary>

##### Parameters

> None

##### Response

> | http code | content-type       |
> | --------- | ------------------ |
> | `200`     | `application/json` |

##### Example cURL

> ```javascript
>  curl -X GET -H "Content-Type: application/json" http://localhost:5000/
> ```

  </details>
  
  <details>
  <summary><code>GET</code> <code><b>/allBerryStats</b></code> <code>(Returns pokeberries statistics)</code></summary>

##### Parameters

> None

##### Response

> | http code | content-type       | response                                                                                                                                                                            |
> | --------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `200`     | `application/json` | `{"berries_names": [...], "min_growth_time": "", "median_growth_time": "", "max_growth_time": "", "variance_growth_time": "", "mean_growth_time": "", "frequency_growth_time": ""}` |

##### Example cURL

> ```javascript
>  curl -X GET -H "Content-Type: application/json" http://localhost:5000/allBerryStats
> ```

  </details>

</br>

> The same endpoints could be used with the Docker IP.

## Graph

You can access to a chart representation of the data obtained from the endpoint /allBerryStats by visiting http://localhost:5000/graph in a web browser.

> The same view can be accessed with the Docker IP.

## Technologies Used

- Flask 3.0.3
- Python 3.10
- Docker 26.0.2
- Pytest 8.1.1
