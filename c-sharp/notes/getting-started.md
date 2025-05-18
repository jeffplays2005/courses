## Using .NET CLI to create a new project

Use the .NET CLI to create a new project. The command will create a new directory with the project name and generate the necessary files for a basic .NET application.

Alternatively can use Visual Studio or Visual Studio Code to create a new project.

```bash
dotnet new <template name>

dotnet build
dotnet run
```

### Introduction to files and foldes

- MyWebApp.csproj - The project file that contains information about the project, such as its dependencies and build settings.
- `.sln` - The solution file that contains information about the solution, such as its projects and build settings.
- `obj` - The object folder that contains intermediate files generated during the build process.
- `Properties/launchSettings.json` - The launch settings file that contains information about how to launch the application, such as the environment variables and command-line arguments.

Example `launchSettings.json` file:

```json
{
  "$schema": "https://json.schemastore.org/launchsettings.json",
  "profiles": {
    "http": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "http://localhost:5218",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "https": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "applicationUrl": "https://localhost:7140;http://localhost:5218",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

### Running the .NET application

Can use something like `dotnet watch`, which will automatically rebuild and restart the application when changes are made to the code. This is similar to `nodemon` for Node.js applications.

```bash
> dotnet watch

Now listening on: http://localhost:5287
```
