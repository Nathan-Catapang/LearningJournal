import cv2
import time
import os
import sys

# Initialize ONLY Side-Profile Cascades (Isolates tracking to left/right ear profile angles)
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR: Could not access your webcam.")
    sys.exit()

# Setup tracking containers
movement_history = []
direction_changes = 0
last_direction = None   
last_seen_time = time.time()

meme_triggered = False
meme_popup_time = 0

print("Glitch-Free Ear Tracker Active! Turn to your side and shake head smoothly. Press 'q' to quit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Run right-facing side profile detection
    profiles_right = profile_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Flip frame horizontally to catch left-facing profiles with the same classifier
    flipped_gray = cv2.flip(gray, 1)
    profiles_left = profile_cascade.detectMultiScale(flipped_gray, 1.3, 5)
    
    target_found = False
    target_x, target_y, target_w, target_h = 0, 0, 0, 0
    
    # Prioritize active ear profiles instead of forward-facing checks
    if len(profiles_right) > 0:
        (target_x, target_y, target_w, target_h) = profiles_right[0]
        target_found = True
        cv2.rectangle(frame, (target_x, target_y), (target_x+target_w, target_y+target_h), (255, 0, 0), 2)
    elif len(profiles_left) > 0:
        (fx, target_y, target_w, target_h) = profiles_left[0]
        target_x = frame.shape[1] - fx - target_w
        target_found = True
        cv2.rectangle(frame, (target_x, target_y), (target_x+target_w, target_y+target_h), (0, 0, 255), 2)

    status_text = "Scanning Ear Profile Shifts..."
    status_color = (0, 255, 255)
    trigger_meme_now = False
    current_time = time.time()
    
    # --- POPUP TIMER ---
    if meme_triggered and (current_time - meme_popup_time >= 1.5):
        try:
            cv2.destroyWindow("WAKE UP!")
        except Exception:
            pass
        meme_triggered = False
        direction_changes = 0
        movement_history.clear()
    
    if target_found:
        last_seen_time = current_time
        ear_profile_center_x = target_x + (target_w // 2)
        cv2.circle(frame, (ear_profile_center_x, target_y + (target_h // 2)), 6, (255, 255, 0), -1)
        
        movement_history.append((current_time, ear_profile_center_x))
        
        # Fixed tuple lookups tracking window
        movement_history = [pt for pt in movement_history if current_time - pt[0] <= 1.5]
        
        if len(movement_history) >= 2:
            diff = movement_history[-1][1] - movement_history[-2][1]
            curr_dir = "right" if diff > 12 else ("left" if diff < -12 else None)
                
            if curr_dir and last_direction and curr_dir != last_direction:
                direction_changes += 1
                last_direction = curr_dir
            elif curr_dir:
                last_direction = curr_dir

        if direction_changes >= 5:
            status_text = "STOP AGREEING!"
            status_color = (0, 0, 255)
            trigger_meme_now = True
            
    else:
        if current_time - last_seen_time > 2.5:
            direction_changes = 0
            movement_history.clear()


    if trigger_meme_now and not meme_triggered:
        meme_path = "c:/Users/Nathan/Downloads/meme.jpg"
        if os.path.exists(meme_path):
            meme_img = cv2.imread(meme_path)
            text = "STOP AGREEING!"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(meme_img, text, (32, 62), font, 1.2, (0, 0, 0), 5, cv2.LINE_AA)
            cv2.putText(meme_img, text, (30, 60), font, 1.2, (0, 0, 255), 3, cv2.LINE_AA)
            cv2.imshow("WAKE UP!", meme_img)
            
            meme_triggered = True
            meme_popup_time = time.time()
            
            direction_changes = 0
            movement_history.clear()
        else:
            print(f"Missing 'meme.jpg' at {meme_path}")

    cv2.putText(frame, f"STATUS: {status_text}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
    cv2.putText(frame, f"Ear Pattern Score: {direction_changes}/5", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.imshow("Ear-Only Profile Trajectory Matrix", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
