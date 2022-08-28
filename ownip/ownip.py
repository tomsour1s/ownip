from .Requests import Requests

class OwnIp:
    @staticmethod
    def get_ip():
        """ Get your current public IP-Address 
        
        Returns:
            JSON Object that contains the IP-Addresse
        """
        instance = Requests()
        return instance.get_ip()