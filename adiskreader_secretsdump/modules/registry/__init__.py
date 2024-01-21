from adiskreader.filesystems import FileSystem
from pypykatz.registry.aoffline_parser import OffineRegistry


class REGSecrets:
    def __init__(self, fs:FileSystem):
        self.__fs = fs
        self.SAM_PATH = '\\Windows\\System32\\config\\SAM'
        self.SECURITY_PATH = '\\Windows\\System32\\config\\SECURITY'
        self.SYSTEM_PATH = '\\Windows\\System32\\config\\SYSTEM'
        self.result = None
    
    async def run(self):
        sys_file = await self.__fs.open(self.SYSTEM_PATH)
        security_file = None
        sam_file = None
        try:
            sam_file = await self.__fs.open(self.SAM_PATH)
        except:
            pass
        try:
            security_file = await self.__fs.open(self.SECURITY_PATH)
        except:
            pass
        
        self.result = await OffineRegistry.from_async_reader(sys_file, sam_reader=sam_file, security_reader=security_file)
        for line in str(self.result).split('\n'):
            yield line
    
    def __str__(self):
        t = '=== REG Secrets ===\r\n'
        t += str(self.result)
        return t
