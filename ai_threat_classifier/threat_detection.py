import cv2
import joblib

# Load object detection model (e.g., MobileNet-SSD)
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")
classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle",
           "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse",
           "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor", "knife"]

# Load risk classifier (if needed)
risk_model = joblib.load('ai_threat_classifier/model.pkl')

def detect_objects_and_classify(frame):
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    objects = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            idx = int(detections[0, 0, i, 1])
            label = classes[idx]
            objects.append(label)

    # Logic to determine threat level
    if "knife" in objects:
        threat = "High"
    elif "person" in objects and "mask" in objects:
        threat = "Medium"
    elif "person" in objects:
        threat = "Low"
    else:
        threat = "No Threat"

    return threat, list(set(objects))
