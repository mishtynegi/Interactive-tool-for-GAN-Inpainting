# Interactive tool for GAN Inpainting
An interactive tool with an implementation of the Generative Image Inpainting algorithm found [here](https://github.com/JiahuiYu/generative_inpainting). This an interactive website for demonstration of inpainting results using models trained on various image data sets. This demo be used for academic purposes only.
 
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
The backend has the following directory structure:

```
├── Interactive_tool-for-GAN-Inpainting
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
│   └── model_logs
│	│   └── release_imagenet_256
│	│   └── release_places2_256
│	│   └── release_celeba_256
│	│   └── release_dtd_256
│   └── neuralgym_logs
│	│   └── <logs will go here>
│   └── views
│	│   └── index.html
│	│   └── style.css
│	│   └── banner.png
│   └── data
│	│   └── <static input data>
```

To run the server, run the following commands in the *root* directory:

```
python server.py
```

The webpage can now be accessed at http://localhost:8080/home/index.html
