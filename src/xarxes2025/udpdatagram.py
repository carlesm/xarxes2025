from time import time

    
class UDPDatagram:	
    HEADER_SIZE = 12
	
    def __init__(self, seqnum, payload):
        self.encode(seqnum, payload)        
        pass
        
    def encode(self, seqnum, payload):
        """Encode the RTP packet with header fields and payload."""
        header = bytearray(self.HEADER_SIZE)

        version = 2
        padding = 0
        extension = 0
        cc = 0
        marker = 0
        pt = 26 # MJPEG (we convert all frames to JPEG)

        # Fill the header bytearray with RTP header fields
        header[0] = (version << 6) | (padding << 5) | (extension << 4) | cc
        header[1] = (marker << 7) | pt
        header[2] = (seqnum >> 8) & 255 #upper bits
        header[3] = seqnum & 255

        # Bytes 4-7 are for the timestamp, in our case, the time() as an int. Its your task to
        # fill this in.
        header[4] = 
        header[5] = 
        header[6] = 
        header[7] = 

        # Bytes 8-11 are for the SSRC, in our case, 0. Its your task to
        # fill this in.
        header[8] = 
        header[9] = 
        header[10] = 
        header[11] = 
        
        self.header = header
        
        # Get the payload from the argument
        self.payload = payload
        
    def decode(self, byteStream):
        """Decode the RTP packet."""
        self.header = bytearray(byteStream[:self.HEADER_SIZE])
        self.payload = byteStream[self.HEADER_SIZE:]

    def get_version(self):
        """Return RTP version."""
        return int(self.header[0] >> 6)

    def get_seqnum(self):
        """Return sequence (frame) number."""
        seqnum = self.header[2] << 8 | self.header[3]
        return int(seqnum)

    def timestamp(self):
        """Return timestamp."""
        timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
        return int(timestamp)

    def get_payload(self):
        """Return payload."""
        return self.payload
        
    def get_datagram(self):
        """Return RTP datagram."""
        return self.header + self.payload