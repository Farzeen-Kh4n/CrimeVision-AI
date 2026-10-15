from app.services.fusion import MultimodalFusion

if __name__ == "__main__":
    fusion = MultimodalFusion()
    
    # Dummy test data
    mock_image = [{"label": "person", "confidence": 0.95}]
    mock_audio = [{"timeline": "Critical Threat", "description": "Weapon mention"}]
    mock_video = [{"time_sec": 0.0, "event": "Audit normal"}]
    
    report = fusion.fuse_evidence(mock_image, mock_audio, mock_video)
    print("Fused Report Generated:", report)
    print("Epic 5 Multimodal Fusion Module is Ready and Working!")
    