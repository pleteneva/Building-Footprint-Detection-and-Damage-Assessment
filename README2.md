## Tast
Detect buildings and assess damage from satellite images after natural disasters.


## Approach

### Building footprint detection
1. To detect buildings in satellite images experimented with pretrained segmentation models:
    - Building_footprint_segmentation library 
        [https://github.com/fuzailpalnak/building-footprint-segmentation]
      - Datasets: 
        - Massachusetts Buildings Dataset
        - Inria Aerial Image Labeling Dataset
    - SegFormer b4 city satellite segmentation
        [https://huggingface.co/ratnaonline1/segFormer-b4-city-satellite-segmentation-1024x1024]
   
   ReFineNet segmentation model from Building_footprint_segmentation library was chosen because it has better results on test dataset. 
    The model was pretrained on Inria Aerial Image Labeling Dataset

Next step:
Fine-tune pretrained segmentation models on the datasets with building footprints, such as:
    - SpaceNet
    - xView
    - OpenStreetMap
    - Bonai [https://github.com/jwwangchn/bonai]
    - Microsoft Building Footprints [https://www.microsoft.com/en-us/maps/bing-maps/building-footprints]
    - Open Cities AI Challenge [https://www.drivendata.org/competitions/60/building-segmentation-disaster-resilience/]
Add classes: car and aircraft:
Potential datasets: xView and Kaggle datasets:
Limitations - only bboxes - so need to convert bboxes to segmentation masks or use object detection models.
To detect buildings in satellite images experiment with pretrained object detection models: YOLOv8 nano as baseline
Add crops different sizes to train dataset to improve model performance on small buildings.
Add pyramids to train dataset to improve model performance on different scales.



### Damage assessment
xView2 dataset [https://xview2.org/dataset]  provided pairs of images pre-disaster and post-disaster 
was labeled with a degree of damage that occurred to it during the disaster, scaled from 1 to 4
(no-damage, minor-damage, major-damage, destroyed)
The approach is localization of buildings and then classification of damage degree for each building.
As models can be used from repositories:
1. Fully convolutional Siamese neural networks for buildings damage assessment from satellite images
[https://github.com/bloodaxe/xview2-solution ]
[https://paperswithcode.com/paper/fully-convolutional-siamese-neural-networks]
2. [https://github.com/DIUx-xView/xView2_baseline]





## Future approaches
### Building footprint detection
1. 
### Damage assessment
Use ChangeFormer [https://github.com/wgcban/ChangeFormer]  to detect changes in buildings before and after disaster.



## Project structure
- `data` - data folder
- `output` - folder with output data: geojson files with building footprints and visualizations
- `src` - source code folder
- `configs` - folder with config 
- `run.sh` - bash script to run the project
- `main.py` - main script to run the project
- `requirements.txt` - requirements file
- `README.md` - readme file
- `Dockerfile` - docker file

## Run prediction
```
bash run.sh
python3 main.py --config path-to-config
```

