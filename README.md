# Abricate --- A Singularity Container

Singularity container for [Abricate]()

## Pre-requisite

Install [Singularity](http://singularity.lbl.gov/docs-installation)

## Usage

### Latest version

The following steps are needed to use the image:

1. Pull the image:

```
singularity pull --name TMP_DIRECTORY shub://phgenomics-singularity/Abricate@latest
```
This will command will create a file `Abricate.simg`, which is executable.

2. Use the image:
```
./Abricate.simg --help
```

### A particular version

```
singularity pull --name mlst shub://phgenomics-singularityAbricate@VERSION.NUMBER
```

## Suggested pattern

1. Create a `singularity` folder:

```
mkdir HOME/singularity
```

2. Pull the image to the `singularity` folder.

```
singularity pull --name Abricate shub://phgenomics-singularity/Abricate@latest
```

3. Link the image to a folder in your `PATH` (e.g., `HOME/bin`)

```
ln -s HOME/singularity/Abricate.simg HOME/bin/Abricate
```

Now, when you login again, you should be able to just type:

```
Abricate --help
```

## Updating the DB

1. `git pull` the latest version of the repo
2. Within the sub-folder of the appropriate version, create a subfolder with date in the following format: `DBYYYYMMDD`
3. Copy the Singularity recipe from another sub-folder in the same version, and rename it so that it has the following format: `Singularity.vXX.X_DBYYYYMMDD` (where `XX.X` corresponds to the version number, and `YYYYMMDD` corresponds to the date.)
