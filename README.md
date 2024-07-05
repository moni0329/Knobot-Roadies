# Smart Cap Project

This project involves the development of a Smart Cap with various functionalities to assist users with navigation and safety. The functionalities include detecting crosswalks, identifying pedestrian traffic light color status, vehicle approaching awareness, and navigating to a destination.

## Functional Requirements

The following mentioned functional requirements were done by 28.06.2024

1. **Detect Crosswalks**: Utilizes a YOLOv5 model to detect crosswalks using satellite images and a camera module.
2. **User Voice Recognition**: Captures and recognizes the user's voice commands.
3. **Speech-to-Text Conversion**: Converts the recognized speech into text for further processing.
4. **User’s Voice Command Processing**: Processes the voice commands to determine actions.
5. **Provide Distance Measurement to Raspberry Pi**: Measures and provides the distance to the Raspberry Pi.
6. **Text-to-Speech Conversion**: Converts text responses into speech to communicate with the user.
7. **Check Vehicle Distance**: Uses ultrasonic sensors to check the distance of approaching vehicles for safety.

## Project Structure

- `detect_crosswalks/`: Directory containing the code for crosswalk detection using YOLOv5.
- `navigation utilities/`: Directory for code with voice recognition, speech-to-text, and text-to-speech conversion.
- `voice_command_processing/`: Directory for processing user voice commands.
- `vehicle_distance_calculation_and_proximity_awareness/`: Directory for code related to distance measurement using ultrasonic sensors and vehicle proximity checking code.
