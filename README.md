# Cookiecutter SAM for Lambda functions with AWS Lambda Powertools Java

This is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM) and Java with [Lambda Powertools Java](https://github.com/awslabs/aws-lambda-powertools-java).

It is important to note that you should not try to `git clone` this project but use `SAM` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Usage

Generate a new SAM based Serverless App: `sam init --location gh:aws-samples/cookiecutter-aws-sam-powertools-java`

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

## Options

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`runtime` | You can choose the target runtime among available [Lambda Java runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
`dependency_manager` | You can choose between Maven and Gradle to manage dependencies for the generated project

# Credits

* This project has been generated with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)

License
-------

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
