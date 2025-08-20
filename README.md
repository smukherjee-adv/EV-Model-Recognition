# EV-Model-Recognition
Electric Vehicle Detection and Recognition using YOLO, with scripts for image collection, training, evaluation, inference, and deployment on Jetson Orin Nano


##  Repository Structure

```plaintext
EV-Recognition/
│
├── dataset/                
│          
│   ├── train/              # Training images
│   ├── val/                # Validation images
│   └── test/               # Test images
│
├── scripts/                
│   ├── dataset_generation.py   # Collection of images
│   ├── augment_images.py   # Augment dataset
│   ├── train_yolo.py       # Train YOLOv8 model
│   ├── evaluate_yolo.py    # Evaluate trained model
│   └── inference_yolo.py   # Run predictions on new images
│
|              
│      
├── Yolo_model_deployment_in_jetson_orin.docs  # Deployemnt instruction
├── requirements.txt        # Required Python packages
└── README.md               # Project overview and instructions
