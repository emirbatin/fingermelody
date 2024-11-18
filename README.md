# 🎵 MelodyFingers

MelodyFingers is an interactive music application that transforms your hand movements into musical notes using computer vision. By detecting your finger positions through your webcam, you can create melodies in real-time with visual feedback. The app uses Mediapipe for precise hand tracking, OpenCV for image processing, and Pygame for sound generation.

Test Video : https://www.youtube.com/watch?v=R-Z08srY3d8

## ✨ Features

- Real-time hand tracking for both hands simultaneously
- 10 different musical notes (5 for each hand)
- Visual feedback with growing/shrinking bubbles for each finger
- Easy-to-understand hand landmark visualization
- Smooth note triggering system with state management
- Interactive bubble animations that respond to your playing

## 🎹 Musical Notes Mapping

Right Hand:
- Thumb: C4
- Index: D4
- Middle: E4
- Ring: F4
- Pinky: G4

Left Hand:
- Thumb: A3
- Index: B3
- Middle: C5
- Ring: D5
- Pinky: E5

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MelodyFingers.git
cd MelodyFingers
```

2. Install required packages:
```bash
pip install opencv-python mediapipe pygame
```

3. Ensure you have the following directory structure:
```
MelodyFingers/
├── main.py
├── notes/
│   ├── A3.mp3
│   ├── B3.mp3
│   ├── C4.mp3
│   ├── C5.mp3
│   ├── D4.mp3
│   ├── D5.mp3
│   ├── E4.mp3
│   ├── E5.mp3
│   ├── F4.mp3
│   └── G4.mp3
```

## 📦 Dependencies

- Python 3.7+
- OpenCV (`cv2`)
- MediaPipe
- Pygame
- Sound files (.mp3 format) for musical notes

## 🎮 Usage

1. Run the script:
```bash
python main.py
```

2. Show your hands to the camera
3. Move your fingers below the 60% height threshold of the camera view to trigger notes
4. Watch the green bubbles grow as you play
5. Press 'ESC' to exit the application

## 🔧 Customization

You can modify these parameters in the code:
```python
min_detection_confidence=0.7  # Hand detection sensitivity
min_tracking_confidence=0.7   # Hand tracking sensitivity
bubble_growth_rate = 10       # How fast bubbles grow when playing
max_bubble_size = 50         # Maximum size of visual feedback bubbles
```

## 🎵 Adding Custom Sounds

To use your own sounds:
1. Place your .mp3 files in the `notes` folder
2. Update the `notes` dictionary in the code with your sound file names
3. Ensure the sound files match the expected format (e.g., "C4.mp3")

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. You can:
- Add new sound effects
- Implement different visual feedback styles
- Improve hand tracking accuracy
- Add new musical features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Hand tracking may be less accurate in low light conditions
- Rapid finger movements might cause sound overlap
- Performance may vary based on computer specifications

## 🙏 Acknowledgments

- MediaPipe team for the hand tracking solution
- OpenCV community
- Pygame developers
- Contributors of the musical note samples

---

**Note**: This project was developed for fun and educational purposes. Feel free to modify and improve the code as you see fit!
