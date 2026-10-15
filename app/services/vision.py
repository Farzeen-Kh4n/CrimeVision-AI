import torch
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection
from PIL import Image

class ImageAnalyzer:
    def __init__(self):
        # Lightweight model jo laptop par easily run ho jaye
        self.model_id = "google/owlvit-base-patch32"
        print("Loading Image Analysis Models...")
        self.processor = AutoProcessor.from_pretrained(self.model_id)
        self.model = AutoModelForZeroShotObjectDetection.from_pretrained(self.model_id)
        print("Models loaded successfully!")

    def detect_objects(self, image_path, target_labels=["person", "weapon", "knife", "gun", "phone"]):
        """
        Epic 2 - Activity 2.1: Detects forensic targets in an image.
        """
        image = Image.open(image_path).convert("RGB")
        
        inputs = self.processor(text=target_labels, images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        
        target_sizes = torch.tensor([image.size[::-1]])
        results = self.processor.post_process_object_detection(
            outputs=outputs, target_sizes=target_sizes, threshold=0.1
        )[0]

        detections = []
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            box_coords = [round(i, 2) for i in box.tolist()]
            detections.append({
                "label": target_labels[label],
                "confidence": round(score.item(), 2),
                "box": box_coords
            })
            
        return detections

    def generate_scene_hypothesis(self, detections):
        """
        Epic 2 - Activity 2.2: Generates scene description and hypotheses.
        """
        labels = [d['label'] for d in detections]
        if not labels:
            return "No critical objects detected in the scene."

        summary = f"Detected key items in the scene: {', '.join(set(labels))}."
        
        hypothesis = "Preliminary Forensic Hypothesis: "
        if any(w in labels for w in ["weapon", "knife", "gun"]):
            hypothesis += "Potential armed incident or threat visual evidence detected."
        elif "person" in labels:
            hypothesis += "Person detected in frame. Requires timeline cross-reference."
        else:
            hypothesis += "Standard visual evidence scene."
            
        return f"{summary} {hypothesis}"