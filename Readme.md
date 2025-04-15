# 👤 Face Recognition System using Python

This is a basic face recognition system built with Python, OpenCV, and the `face_recognition` library (based on dlib). It can detect and recognize human faces in real-time from your webcam feed by comparing them with known images.

---

## 🗂 Project Structure

Face Recognition/ ├── facerecog.py # Main script ├── known_faces/ # Folder with known face images (e.g., messi.jpg, neymar.jpg) ├── dlib_env/ # Python virtual environment ├── README.md # Project documentation

---

## 🔧 Dependencies

- face_recognition
- opencv-python
- dlib
- numpy

---

## 🛠️ Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/face-recognition.git
   cd face-recognition
   python -m venv dlib_env
   .\dlib_env\Scripts\activate
   pip install face_recognition opencv-python
   python facerecog.py
   ```

📸 How It Works
Loads and encodes images from the known_faces/ folder.

```

Captures webcam feed.

Detects and matches faces frame-by-frame.

Draws rectangles and displays names of recognized individuals.

➕ Add More Faces
Place clear, front-facing photos into the known_faces/ folder.

Update the face loading logic in facerecog.py with new names/images.
'''

🙋‍♂️ Author
Gowtham Ramakrishna Rayapureddi

📜 License
MIT License – free to use and modify.

🙏 Acknowledgments
face_recognition

OpenCV

dlib

Let me know if you want a `requirements.txt` too, or help linking the GitHub repo!
```
