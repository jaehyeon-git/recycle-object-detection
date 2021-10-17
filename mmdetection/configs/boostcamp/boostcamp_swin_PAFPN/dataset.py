_base_ = '/opt/ml/detection/object-detection-level2-cv-01/configs/boostcamp/dataset.py'
train_pipeline = [
    dict(type = 'Mosaic', img_scale = (2048,2048)),
    dict(type='Resize', img_scale=(224,224), keep_ratio=True),
]
test_pipeline = [
    dict(
        img_scale=(224,224),
        )
]
