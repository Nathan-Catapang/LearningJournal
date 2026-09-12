# ProfileFace Shift Detector

A real-time computer vision engine written in Python utilizing OpenCV to isolate human profile dynamics. The application analyzes horizontal spatial trajectory shifts via side-profile cascades to detect repetitive head movement patterns (e.g., continuous nodding or shaking) and deploys an automated contextual response window.

---

## Technical Architecture

* **Dual-Aspect Profile Inference:** Bypasses frontal facial recognition entirely. Uses `haarcascade_profileface` executed against standard and horizontally flipped matrices to monitor left and right structural ear/profile boundaries concurrently using a single classifier.
* **Rolling Temporal Vector Window:** Coordinates are captured inside a dynamic array constrained via list comprehension to a strict rolling 1.5-second time-to-live (TTL) window.
* **Directional Delta Evaluation:** Measures coordinate variance across consecutive frames. Direction switches are logged only if horizontal movement deltas break a preset pixel threshold (`> 12` or `< -12`).
* **Self-Healing State Machine:** If target tracking is dropped for more than 2.5 seconds, all spatial histories and directional counters clear automatically to maintain state integrity.

---

## Prerequisites & Installation

### Dependency Installation
Ensure Python 3.8+ is installed on the local system. Install the OpenCV core package via `pip`:

```bash
pip install opencv-python
```

### Resource Directory Structure
The application requires a base image file to act as the automated canvas layout. Verify that the absolute path to the local asset is configured correctly within the source code:

```python
meme_path = "path/to/your/image.jpg"
```

---

## Configuration & Deployment

Execute the runtime module from the terminal interface:

```bash
python main.py
```

### Runtime Control Interface
* **Profile Acquisition:** Position the subject perpendicular to the image sensor (profile perspective). The UI displays a bounding box reflecting orientation status (Blue for right-facing profiles, Red for left-facing profiles).
* **Threshold Execution:** Execute 5 successive horizontal direction alternations within the active window to hit full cadence scoring (`5/5`).
* **Automated Cycle Dismissal:** Once triggered, an overlay engine injects text maps onto the source image canvas, holds the window surface loop for 1.5 seconds, and cleanly purges the UI loop using a non-blocking exception safety wrapper.
* **Process Termination:** Focus the primary display window and press **`q`** to close the video capture hardware bindings.

---

## System Telemetry Metrics

| Metric | Target | Description |
| :--- | :--- | :--- |
| `Status Text` | Live State | Outputs active sensor scanning, orientation metrics, or system break states. |
| `Ear Pattern Score` | Integer Ratio | Numerical log tracking registered directional cuts against the trigger limit. |
