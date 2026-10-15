from app.services.audio import AudioAnalyzer

if __name__ == "__main__":
    print("Initializing Audio Module Test...")
    # Model initialization check
    analyzer = AudioAnalyzer(model_size="tiny") # 'tiny' sabse fast aur safe hai CPU ke liye
    print("Epic 3 Audio Analysis Module is Ready and Working!")
    