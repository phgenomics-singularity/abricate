# Abricate --- A Singularity Container

[![https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg](https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg)](https://singularity-hub.org/collections/1288)

Singularity container for [Abricate](https://github.com/tseemann/abricate)

## Pre-requisite

Install [Singularity](http://singularity.lbl.gov/docs-installation)

## Usage

### Latest version

The following steps are needed to use the image:

1. Pull the image:

    ```bash

    singularity pull --name TMP_DIRECTORY shub://phgenomics-singularity/Abricate@latest

    ```

    This will command will create a file `Abricate.simg`, which is executable.

2. Use the image:

    ``` bash

    ./Abricate.simg --help

    ```

### A particular version

```bash

singularity pull --name mlst shub://phgenomics-singularityAbricate@VERSION.NUMBER

```

## Suggested pattern

1. Create a `singularity` folder:

    ```bash

    mkdir HOME/singularity

    ```

2. Pull the image to the `singularity` folder.

    ```bash

    singularity pull --name Abricate shub://phgenomics-singularity/Abricate@latest

    ```

3. Link the image to a folder in your `PATH` (e.g., `HOME/bin`)

    ```bash

    ln -s HOME/singularity/Abricate.simg HOME/bin/Abricate

    ```

Now, when you login again, you should be able to just type:

```bash

    abricate --help

```

## Updating the DB

1. Run the `update_db.py` script (default version is 0.8 at the moment)
