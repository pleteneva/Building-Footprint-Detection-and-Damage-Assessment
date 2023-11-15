## Tast
Detect buildings footprint and assess damage from satellite images after natural disasters.


## Approach

### Building footprint detection
Experimenting with pretrained segmentation models to detect buildings in satellite images, the following approaches 
were explored:\
    - Building_footprint_segmentation library ([GitHub](https://github.com/fuzailpalnak/building-footprint-segmentation)), datasets: Massachusetts Buildings Dataset, Inria Aerial Image Labeling Dataset\
    - SegFormer b4 city satellite segmentation from HuggingFace ([HuggingFace Model Hub](https://huggingface.co/ratnaonline1/segFormer-b4-city-satellite-segmentation-1024x1024))\
   After evaluation, the ReFineNet segmentation model from the Building_footprint_segmentation library 
was selected due to its better performance on the test dataset. This model was pretrained on the 
Inria Aerial Image Labeling Dataset.

#### Next Steps:
Improve model using additional data:\
To enhance the model's performance, the next step would involve fine-tuning on datasets featuring building footprints, 
including but not limited to:\
    - SpaceNet\
    - xView\
    - OpenStreetMap\
    - Bonai [GitHub](https://github.com/jwwangchn/bonai)\
    - Microsoft Building Footprints [Microsoft BF](https://www.microsoft.com/en-us/maps/bing-maps/building-footprints)\
    - Open Cities AI Challenge [DrivenData](https://www.drivendata.org/competitions/60/building-segmentation-disaster-resilience/)\
Additionally, introduce new categories: car and aircraft, utilizing xView and Kaggle datasets 
as potential sources [Planes in Satellite Imagery](https://www.kaggle.com/datasets/aceofspades914/cgi-planes-in-satellite-imagery-w-bboxes/data), 
[Planes in Satellite Imagery](https://www.kaggle.com/datasets/rhammell/planesnet/code), 
[Spatial Vehicle Detection](https://www.kaggle.com/datasets/sadhliroomyprime/spatial-vehicle-detection). Keep in mind the limitation of having only bounding boxes; 
a workaround involves converting these boxes into segmentation masks or employing object detection models.
For the identification of buildings in satellite images, conduct experiments using pretrained object detection models, 
with YOLOv8 nano or segmentation model HRNet serving as the baseline.

Improve quality during training:
- Enhance the training dataset by adding crops of various sizes to improve the model's effectiveness in 
detecting small buildings. 
- Add pyramid to improve model performance on different scales.


### Damage assessment
The approach is localization of buildings and then classification of damage degree for each building.
To classify the damage degree, the xView2 dataset can be used. 
This dataset [xView](https://xview2.org/dataset), includes pairs of images captured before and after a disaster. 
Each image is labeled with the degree of damage it incurred during the disaster, categorized on a scale from 1 to 4, 
indicating no damage, minor damage, major damage, or complete destruction.
As models can be used from repositories as is:
- Fully convolutional Siamese neural networks for buildings damage assessment from satellite images:
  - [GitHub](https://github.com/bloodaxe/xview2-solution), [PapersWithCode](https://paperswithcode.com/paper/fully-convolutional-siamese-neural-networks)
- xView2 baseline [GitHub](https://github.com/DIUx-xView/xView2_baseline)

To improve quality, the following model can be used:
- ChangeFormer [GitHub](https://github.com/wgcban/ChangeForm)  to detect changes in buildings before and after disaster, and classify damage degree 
afterward.


## Project structure
- `data` - data folder
- `output` - folder with output data: geojson files with building footprints and visualizations
- `src` - source code folder
- `configs` - folder with config 
- `run.sh` - bash script to run the project
- `main.py` - main script to run the project
- `README.md` - readme file
- `Dockerfile` - docker file

## Run prediction for detect buildings footprint
```
bash run.sh
python3 main.py --config path-to-config
```
