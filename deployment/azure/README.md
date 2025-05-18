# Azure Deployment

## Use Azure Container Registry to store a container

- `az acr create` - Creates a new Azure Container Registry. E.g. `az group create --name mygroup --location westus`, `az acr create --name <unique name> --resource-group mygroup --sku standard --admin-enabled true`.
  Azure Container Registry repositories are private, so you need to use the `--admin-enabled` flag to enable admin access. This will create a new user with the username `admin` and a password that is generated for you. Will need to use `docker login myregistry.azurecr.io`.

  To obtain this info, `az acr credential show --name myregistry --resource-group mygroup`.

  The `docker tag` command is used to tag an image with a new name. This is useful for pushing the image to a different registry or for versioning the image. The command takes two arguments: the name of the image to tag and the new name for the image.

  ```bash
  docker tag reservationsystem myregistry.azurecr.io/reservationsystem:v2
  ```

  After running the tag command, you can push the image to the registry using the `docker push` command. This will upload the image to the registry and make it available for use in Azure.

  ```bash
  push myregistry.azurecr.io/reservationsystem:v2
  ```

  Can check if the image was uploaded correctly.

  ```bash
  az acr repository list --name myregistry --resource-group mygroup
  ```
