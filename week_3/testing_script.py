class Client():
    """Class managing clients personal information"""

    def __init__(self, name, ssn):
        """Initiate Client with name and social security number"""

        self.__name = name
        self.__ssn = ssn

    def organization(self, organization_name):
        """Add organization of the client"""

        self.__organization_name = organization_name

client = Client("John Johnson", "111-22-3333")
client.organization = "Microsoft"
print(client)
