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
│   ├── collect_images.py   # Collect images via Excel / Google
│   ├── augment_images.py   # Augment dataset (optional)
│   ├── train_yolo.py       # Train YOLOv8 model
│   ├── evaluate_yolo.py    # Evaluate trained model
│   └── inference_yolo.py   # Run predictions on new images
│
├── docs/                   
│   └── deployment.md       # Deployment instructions
│
├── requirements.txt        # Required Python packages
└── README.md               # Project overview and instructions
