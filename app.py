import cv2
import os
import mediapipe as mp
import pygame
import time

NOTES_FOLDER = "notes"


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

pygame.mixer.init()

notes = {
    "right_thumb": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "C4.mp3")),   
    "right_index": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "D4.mp3")),   
    "right_middle": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "E4.mp3")),  
    "right_ring": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "F4.mp3")),    
    "right_pinky": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "G4.mp3")),   
    "left_thumb": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "A3.mp3")),    
    "left_index": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "B3.mp3")),    
    "left_middle": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "C5.mp3")),   
    "left_ring": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "D5.mp3")),     
    "left_pinky": pygame.mixer.Sound(os.path.join(NOTES_FOLDER, "E5.mp3")),    
}


bubble_sizes = {key: 10 for key in notes.keys()}  
bubble_growth_rate = 10  
max_bubble_size = 50  


cap = cv2.VideoCapture(0)


last_finger_state = {}


while True:
    success, img = cap.read()
    if not success:
        break

    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            hand_label = handedness.classification[0].label  

            
            fingers = {
                "thumb": hand_landmarks.landmark[4],  
                "index": hand_landmarks.landmark[8],  
                "middle": hand_landmarks.landmark[12],  
                "ring": hand_landmarks.landmark[16],  
                "pinky": hand_landmarks.landmark[20],  
            }

            
            for finger_name, landmark in fingers.items():
                x, y = int(landmark.x * img.shape[1]), int(landmark.y * img.shape[0])

                
                if y > img.shape[0] * 0.6:  
                    note_key = f"{hand_label.lower()}_{finger_name}"
                    if note_key in notes:
                        
                        if last_finger_state.get(note_key, False) == False:
                            notes[note_key].play()
                            bubble_sizes[note_key] = min(bubble_sizes[note_key] + bubble_growth_rate, max_bubble_size)
                            last_finger_state[note_key] = True
                else:
                    
                    last_finger_state[f"{hand_label.lower()}_{finger_name}"] = False

                
                bubble_size = bubble_sizes.get(f"{hand_label.lower()}_{finger_name}", 10)
                cv2.circle(img, (x, y), bubble_size, (0, 255, 0), -1)

    
    cv2.imshow("MelodyFingers", img)

    
    if cv2.waitKey(1) & 0xFF == 27:  
        break

    
    for key in bubble_sizes.keys():
        bubble_sizes[key] = max(bubble_sizes[key] - 1, 10)  


cap.release()
cv2.destroyAllWindows()
