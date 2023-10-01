## SPF-MLAdversary

## Overview

**Objective**: This project aims to develop various adversarial attacks against an image classifier to significantly reduce its performance, followed by enhancing its adversarial robustness.

**Team members**:
1. Priyanka Ghosh Dastidar
2. Subhankar Ghosh
3. Farooq Mousal Gessa

The project employs a Python web framework called Flask to create an API for interacting with the machine learning model, including uploading images for classification.

**Technologies used**:
- Flask
- Flask-SQLAlchemy
- TensorFlow
- OpenCV

## Installation

Before installing the project dependencies, it's recommended to create a virtual environment. You can do this by running the following command:

```shell
python3 -m venv venv
```

To install the project dependencies, execute:

```shell
pip install -r requirements.txt
```

Then, activate the virtual environment (assuming a Linux environment):

```shell
source venv/bin/activate
```

## Running the Project

To start the API server, run the following command:

```shell
flask run --app api run
```

By default, the server will be available at http://localhost:5000.

After the server has started, you can interact with the machine learning model using a CLI interface. However, before getting started, users must register an account by providing both a name and a password. Both of these should be placed in the `.env` file located in the root of the CLI project. Ensure you rename the `.env.template` to `.env`. After entering your name and password, run the following command in a separate terminal (don't forget to activate the virtual environment):

```shell
python -m cli register
```

After successful registration, users need to request a unique token to be generated for them. This token will be used in all subsequent requests to the server. To obtain the token, run the following command:

```shell
python -m cli request_token
```

The response will contain your token; copy and paste it into the `.env` file.

At this point, you can start sending images one at a time to the server for classification, like so:

```shell
python -m cli classify --image <path-to-image>/test_images/forest.jpg
```

We have included test images in the `test_images` folder at the root of the project, but feel free to use your own.