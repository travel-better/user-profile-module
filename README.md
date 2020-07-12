# User Profile API

## Description
Simple API to access the User Profiles Database and perform CRUD operations.
Uses Blueprint system to make the application modular, all modules are located in the `app` directory

## Getting started
### Prerequisites
* python3.6
* virtual environment
* pip

Clone the repository and cd to directory

## Running the App
* Create a virtual environment

    ```python3.6 -m venv --without-pip virtual```

* Activate the virtual environment using 

    ```source virtual/bin/activate```

* Download pip in our environment using 

    ```curl https://bootstrap.pypa.io/get-pip.py | python```

* Install all the dependencies from the requirements.txt file by running 

    ```pip install -r requirements.txt```

* Run command to start the app

    ```python3 manage.py server```

By default the application runs on port 5000

### Endpoints

- api/v1/userprofile    : Accepts ['GET', 'POST]
    * This endpoint is used to create a userprofile and list all the user profiles available
    * Note: For a `GET` request, create a `userprofile` design document and a view named `all`; Add the map function as below
    ```
    function (doc) {
        emit(doc.username, doc);
    }
    ```

- api/v1/userprofile/<string:profile_id>    : Accepts  ['GET', 'PUT', 'DELETE']
    * This endpoint is used to view a specific userprofile(specified by the provided profile_id string), update the profile or delete the profile


- Sample JSON data
```
{
    "username": "test",
    "bio": "This is a test bio",
    "total_reward_points": 20.0,
    "current_redeemable_points": 33.5,
    "user_total_carbon_footprint": 1500.99,
    "total_possible_carbon_footprint": 1200.87,
    "total_carbon_footprint_reduced": 200.22,
    "total_user_activities": 2,
    "activities": [
        {
            "activity_name": "Running",
            "activity_destination": "Destination",
            "activity_completed": true,
            "activity_route_taken": "Route",
            "activity_time_taken": 40,
            "activity_total_possible_carbon": 5000.50,
            "activity_carbon_used": 300.50,
            "activity_reward_points": 100.20
        }
    ],
    "points": [
        {
            "total_points": 300.79,
            "redeem_item": "Clothes"
        }
    ]
}
```
