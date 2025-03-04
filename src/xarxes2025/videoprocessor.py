import cv2
from loguru import logger



class VideoProcessor(object):

    ready = False

    def __init__(self, filename):
        """
        Constructor for VideoProcessor object.

        :param filename: The name of the video file to open.
        """
        self.filename = filename
        logger.debug(f"VideoProcessor created for {self.filename}")
        self.cap = cv2.VideoCapture(self.filename)
        if not self.cap.isOpened():
            logger.error(f"Cannot open {self.filename} file")
            raise IOError
        self.frame_num = 0
        self.ready = True

    def next_frame(self):
        """
        Read the next frame from the video file, resize it, encode it as JPEG,
        and return the encoded bytes.

        The function reads a frame from the video, resizes it to fit UDP size
        limits, encodes it as a JPEG image, and returns the byte data. If the
        video file cannot be read or the frame cannot be encoded, an error is
        logged and an IOError is raised.

        :returns: JPEG-encoded byte data of the next frame, or None if the end 
                of the video is reached.
        """
        # Get next frame from the videofile
        ret, frame = self.cap.read()
        if not ret:
            return None

        self.frame_num += 1
        
        # Resize for UDP size limits
        # If using bigger frames, the UDP packets will have to be fragmented 
        # and reassembled on the other side, that is out of the scope for 
        # this course.
        frame = cv2.resize(frame, (500, 380)) 
    
        ret, encoded_frame = cv2.imencode('.jpg', frame)
        if not ret:
            logger.error(f"Cannot encode frame {self.frame_num}")
            raise IOError

        jpeg_bytes = encoded_frame.tobytes() # Get the bytes

        data = jpeg_bytes
        return data
        
    def get_frame_number(self):
    """Return the current frame number being processed."""

        return self.frame_num

