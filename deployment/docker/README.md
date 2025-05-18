# Docker

A tool for running containerized apps. Incldues the app and filesystem that makes the environment where it runs.

Typically smaller footprint than a VM, and faster to start up. This is because the VM has to load the entire OS, while a container only loads the app and its dependencies.

To build a docker container, you need to create a Dockerfile. This is a text file that contains the instructions for building the container(including the files). The Dockerfile is used by the docker build command to create the container.

> [!IMPORTANT]
> Docker is not a virtual machine. It is a container. A container is a lightweight, portable, and self-sufficient unit that can run any application. However, Docker ensures that the container runs in a consistent environment, regardless of the host operating system; unless configured otherwise.

## Registry

The most well known registry for docker images is Docker Hub.

For ASP.NET Core Runtime Docker images, there are two main versions that are LTS(long term support).

8.0 (Long-Term Support): mcr.microsoft.com/dotnet/aspnet:8.0
6.0 (Long-Term Support): mcr.microsoft.com/dotnet/aspnet:6.0

## CLI

- `docker pull` - Pulls an image from a registry. E.g. `docker pull mcr.microsoft.com/dotnet/aspnet:8.0`
- `docker image list` - Lists all images on the local machine.
- `docker run` - Runs a container from an image. E.g. `docker run mcr.microsoft.com/dotnet/samples:aspnetapp`
  > [!NOTE]
  > By default, Docker doesn't allow for inbound network requests to reach the container. You can use the `-p` flag to map a port on the host machine to a port on the container. E.g. `docker run -p 8080:80 mcr.microsoft.com/dotnet/samples:aspnetapp` will map port 8080 on the host machine to port 80 on the container.
- `docker ps` - Lists all running containers.
- `docker stop <pid>` - Stops a running container. E.g. `docker stop 1234`
- `docker start <pid>` - Starts a stopped container. E.g. `docker start 1234`
- `docker rm <pid>` - Removes and cleans up resources from a container. E.g. `docker rm 1234`
- `docker container rm -f <pid>` - Force removes a running container and all its resources.
- `docker image rm <image>` - Removes an image from the local machine. E.g. `docker image rm mcr.microsoft.com/dotnet/samples:aspnetapp`

### Examples

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:6.0
WORKDIR /app
COPY myapp_code .
RUN dotnet build -c Release -o /rel
EXPOSE 80
WORKDIR /rel
ENTRYPOINT ["dotnet", "myapp.dll"]
```

| Command        | Action                                                                         |
| -------------- | ------------------------------------------------------------------------------ |
| `FROM`         | Specifies the base image to use.                                               |
| `WORKDIR`      | Sets the working directory; used by subsequent commands.                       |
| `COPY <a> <b>` | Copies files from the host machine to the container.                           |
| `RUN`          | Runs a command in the container.                                               |
| `EXPOSE`       | Exposes a port on the container.                                               |
| `ENTRYPOINT`   | Sets the command to run when the container starts. Needs to be a string array. |

### Compatibility

Docker can be built for either Linux or Windows. The default is Linux, but you can specify the OS in the Dockerfile.
