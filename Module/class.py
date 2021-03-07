{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        },
        {
            "name": "Flask: Hello World",
            "type": "python",
            "request": "launch",
            "module" : "flask",
            "env" : {
                "FLASK_APP" : "${workspaceFolder}/Week9/helloWorldFlask.py",
                "FLASK_ENV" : "development",
                "FLASK_DEBUG" : "0"
            },
            "args" : [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja" : true
        }
    ]
}



