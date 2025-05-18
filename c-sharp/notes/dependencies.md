## Installing dependencies

Can optionally use `--version=<version number/range>` to specify a version or version range.

Can also install the latest available version using `--prerelease`.

```
dotnet add package <package name>

> dotnet add package Humanizer

info : PackageReference for package 'Humanizer' version '2.11.10' updated in file 'C:\Users\username\Desktop\DotNetDependencies\DotNetDependencies.csproj'.
```

## Semantic versioning

Semantic versioning is a versioning scheme for software that uses a three-part version number: MAJOR.MINOR.PATCH. The rules are as follows:

- MAJOR version changes indicate incompatible API changes.
- MINOR version changes indicate backward-compatible new features.
- PATCH version changes indicate backward-compatible bug fixes.

## Configure the project file for update

| Notation  | Applied rule  | Description                                           |
| --------- | ------------- | ----------------------------------------------------- |
| 1.0       | x >= 1.0      | Minimum version, inclusive                            |
| (1.0,)    | x > 1.0       | Minimum version, exclusive                            |
| [1.0]     | x == 1.0      | Exact version match                                   |
| (,1.0]    | x ≤ 1.0       | Maximum version, inclusive                            |
| (,1.0)    | x < 1.0       | Maximum version, exclusive                            |
| [1.0,2.0] | 1.0 ≤ x ≤ 2.0 | Exact range, inclusive                                |
| (1.0,2.0) | 1.0 < x < 2.0 | Exact range, exclusive                                |
| [1.0,2.0) | 1.0 ≤ x < 2.0 | Mixed inclusive minimum and exclusive maximum version |
| (1.0)     | invalid       | invalid                                               |

## Listing and finding outdated packages

```
> dotnet list package --outdated

Top-level Package      Requested   Resolved   Latest
> Humanizer            2.7.*       2.7.9      2.8.26
```

## Example dependencies file

`DotNetDependencies.csproj`

```xml
<ItemGroup>
    <PackageReference Include="Humanizer" Version="2.7.9" />
</ItemGroup>
```
