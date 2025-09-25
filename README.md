The following components are on the **free hosted tier level** of [Render](https://render.com/) and are shutdown when not in use.  Accessing each component from a shutdown state requires it to spin back up and this can **delay requests for a minute or so**.

- [FastAPI API](https://sort-demo.onrender.com/docs) - [code](https://github.com/Siliconrob/sort-demo) built with [FastAPI](https://fastapi.tiangolo.com/)

## Improvement

Add in restricted authorization API or tokens

## Demo use

![fastapi](https://github.com/user-attachments/assets/c4d6b33b-ed18-43d4-b02b-74f9bfeb1d5b)

## Flow

This API was built on top of FastAPI which is my favorite framework when working with Python.  It is everything that a modern web API should be and is built for maximum productivity with all the correct options builtin to get you off and running along with being setup for long term success i.e. batteries included.

## Development

This project was built using the default FastAPI template.  Download Python 3.13 and I am using [PyCharm](https://www.jetbrains.com/pycharm/) to run the program.  You could use any tool you wish that will open the folder

## Render Deployment

- Signup for a free [Render](https://dashboard.render.com/register) account.  You won't regret it :)
- Connect your [GitHub](https://docs.render.com/github) account
- Choose the `Web Services` [option](https://docs.render.com/web-services)
 - Make sure it is set to `Python 3`
 - Setup a name
 - Set the `Start Command` to `uvicorn main:app --host 0.0.0.0 --port $PORT`
