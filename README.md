# GAN Inpainting
 
## Prerequisites:
- Bash Shell
- Anaconda

## Preparing the environment: 
Run the following commands in your shell:

```
conda config –add channels conda-forge
conda install tensorflow
conda install opencv
conda install pyyaml
pip install git+https://github.com/JiahuiYu/neuralgym
conda install pybottle
```

## Running the server:
The server has the following directory structure:

```
├── *Interactive_tool-for-GAN-Inpainting*
│   ├── server.py
│   └── test.py
│   └── inpaint.yml
│   └── inpaint_ops.py
│   └── inpaint_model.py
│   └── input.png
│   └── inputA.png
│   └── inputB.png
│   └── output.png
│   └── output.png
│   └── output2.png
│   └── *model_logs*
│	│   └── release_imagenet_256
│	│   └── release_places2_256
│	│   └── release_celeba_256
│	│   └── release_dtd_256
│	└── *neuralgym_logs*
│	│   └── _<logs will go here>_
│   └── *views*
│	│   └── index.html
│	│   └── style.css
│	│   └── banner.png
│   └── *data*
│	│   └── _<static input data>_
```

To run the server, run the following commands in the *GeneratingInpainting* directory:

```
python server.py
```

The webpage can now be accessed at http://localhost:8080/home/index.html	

## Running the training:
For the training, the following directory structure is required: 

```
├── *Interactive_tool-for-GAN-Inpainting*
│   ├── train.py
│   └── test.py
│   └── inpaint.yml
│   └── inpaint_ops.py
│   └── inpaint_model.py
│   └── *model_logs*
│	│   └── _<model directories go here>_
│	└── *neuralgym_logs*
│	│   └── _<logs will go here>_
│	└── *data*
│	│   └── _training and validation sets>_
│	│   └── _<flist files for the same>_
```

To run this, modify _inpaint.yml_ to point to your data sets located above (see our _inpaint.yml_ file for an example with the ‘dtd’ data set). Details for creating an flist file can be found here.

Once the properties have been set, run the following command in the GenerativeInpainting directory:
```
python train.py
```
