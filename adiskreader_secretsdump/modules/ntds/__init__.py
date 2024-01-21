from adiskreader.filesystems import FileSystem
from pypykatz.registry.aoffline_parser import OffineRegistry
from aesedb.eesentdb import ESENT_DB
from aesedb.security.ntds import NTDS


class NTDSSecrets:
    def __init__(self, fs:FileSystem, bootkey:bytes or str or OffineRegistry):
        self.__fs = fs
        self.bootkey = bootkey
        self.NTDS_PATH = '\\Windows\\NTDS\\ntds.dit'
        self.with_history = True
        self.ignore_errors = True
        self.result = None
    
    async def run(self):
        if isinstance(self.bootkey, OffineRegistry):
            bootkey = await self.bootkey.system.get_bootkey()
        elif isinstance(self.bootkey, str):
            bootkey = bytes.fromhex(self.bootkey)
        elif isinstance(self.bootkey, bytes):
            bootkey = self.bootkey
        else:
            raise Exception('Invalid bootkey type! %s' % type(self.bootkey))
        
        try:
            ntds_file = await self.__fs.open(self.NTDS_PATH)
            if ntds_file is None:
                raise Exception('NTDS file not found!')
        except Exception as e:
            raise e

        
        db = ESENT_DB(ntds_file)
        _, err = await db.parse()
        if err is not None:
            raise err
                
        ntds = NTDS(db, bootkey)
        print('Dumping secrets')
        async for secret, err in ntds.dump_secrets(with_history=self.with_history, ignore_errors = self.ignore_errors):
            if err is not None:
                raise err

            if secret is None:
               continue

            for line in str(secret).split('\n'):
                yield line.strip()
    
    def __str__(self):
        t = '=== NTDS Secrets ===\r\n'
        t += 'Not stored in memory!'
        return t
