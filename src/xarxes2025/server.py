from loguru import logger
# from xarxes2025.udpdatagram import UDPDatagram
# from xarxes2025.videoprocessor import VideoProcessor


class Server(object):
    def __init__(self, port):       
        """
        Initialize a new VideoStreaming server.

        :param port: The port to listen on.
        """

        logger.debug(f"Server created ")
        
    

    # # 
    # # This is not complete code, it's just an skeleton to help you get started.
    # # You will need to use these snippets to do the code.
    # # 
    # #     
    # def send_udp_frame(self):
      
    #     # This snippet reads from self.video (a VideoProcessor object) and prepares 
    #     # the frame to be sent over UDP. 

    #     data = self.video.next_frame()
    #     if data:
    #         if len(data)>0:
    #                 frame_number = self.get_frame_number()
    #                 # create UDP Datagram

    #                 udp_datagram = UDPDatagram(frame_number, data).get_datagram()

    #                 # send UDP Datagram
    #                 socketudp.sendto(udp_datagram, (address, port))
                        
